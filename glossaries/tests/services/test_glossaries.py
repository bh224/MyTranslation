from rest_framework.test import APITestCase
from glossaries.models import Category, Glossary
from glossaries.services.glossary_service import get_glossary_by_category
from users.models import User
from projects.models import Project


class TestGlossary(APITestCase):
    def create_a_user(self, username, is_admin):
        user = User.objects.create(
            username=username, password="1234", is_admin=is_admin
        )
        return user

    def create_a_project(self, category, title, description, uploader):
        project = Project.objects.create(
            category=category, title=title, description=description, uploader=uploader
        )
        return project

    def test_add_a_category(self) -> None:
        # Given
        user = self.create_a_user("test_user0", False)
        project = self.create_a_project("webtoon", "webtoon_title", "kor->jpn", user)

        # When
        category = Category.objects.create(project=project, name="지역", author=user)

        # Then
        self.assertEqual(category.name, "지역")

    def test_add_a_word_to_glossary(self) -> None:
        # Given
        user = self.create_a_user("test_user", False)
        project = self.create_a_project("game", "game_title", "kor->jpn", user)
        category = Category.objects.create(project=project, name="인물", author=user)
        Glossary.objects.create(
            project=project,
            category=category,
            origin_word="은정",
            furigana="ふくやま りさ",
            trans_word="福山梨沙",
            details="주인공/여/18세",
            author=user,
        )

        # When
        glossary = Glossary.objects.filter(project=project.pk)

        # Then
        self.assertEqual(len(glossary), 1)
        self.assertEqual([word.origin_word for word in glossary], ["은정"])

    def test_get_glossary_of_a_project(self) -> None:
        # Given
        user = self.create_a_user("test_user2", False)
        project = self.create_a_project("webtoon", "fantasy", "kor->jpn", user)
        category1 = Category.objects.create(project=project, name="인물", author=user)
        category2 = Category.objects.create(project=project, name="지역", author=user)
        [Glossary.objects.create(
            project=project,
            category=category1,
            origin_word=f"이름{i}",
            furigana="ふくやま りさ",
            trans_word=f"福山梨沙{i}",
            details="주인공/여자",
            author=user,
        ) for i in range(1, 6)]
        [Glossary.objects.create(
            project=project,
            category=category2,
            origin_word=f"서울{i}",
            furigana="みなみかわ",
            trans_word=f"南珂倭{i}",
            details="실제지역명 사용x 상용한자 아닌 걸로 대체",
            author=user,
        ) for i in range(1, 6)]
        
        # When
        glossary_by_character = get_glossary_by_category(project.pk, category1.pk)
        glossary_by_place = get_glossary_by_category(project.pk, category2.pk)

        # Then
        self.assertEqual([i.trans_word for i in glossary_by_character][0], "福山梨沙1")
        self.assertEqual([i.trans_word for i in glossary_by_place][0], "南珂倭1")

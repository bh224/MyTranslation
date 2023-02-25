from rest_framework.test import APITestCase
from glossaries.models import Category, Glossary
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

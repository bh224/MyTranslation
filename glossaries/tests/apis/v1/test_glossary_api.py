from urllib import response
from rest_framework.test import APITestCase
from users.models import User
from projects.models import Project
from glossaries.models import Glossary, Category

class TestGlossaryAPI(APITestCase):
    def create_a_user(self, username, is_admin): 
        user = User.objects.create(username=username, is_admin=is_admin)
        user.set_password("1234")
        user.save()
        self.client.force_login(user)
        return user
    
    def create_a_project(self, category, title, description, uploader):
        project = Project.objects.create(
            category=category, title=title, description=description, uploader=uploader
        )
        return project
    
    def test_add_a_category_and_a_word_to_glossary(self) -> None:
        # Given
        user = self.create_a_user("test_user1", False)
        project = self.create_a_project("웹툰", "판타지여동생", "네이버웹툰/한일/연재중", uploader=user)

        # 카테고리 등록
        # When
        category_response = self.client.post(
            f"/api/v1/projects/{project.pk}/categories",
            data={
                "name":"인물"
            }
        )
        result_category = category_response.json()

        # Then
        self.assertEqual(result_category["name"], "인물")

        # 글로서리 용어 추가
        # When
        glossary_response = self.client.post(
            f"/api/v1/projects/{project.pk}/glossaries",
            data={
                "category_pk": result_category["pk"],
                "origin_word": "우리 고등학교",
                "trans_word": "宇理 高校",
                "furigana": "うり",
                "details": "실제 존재하지 않는 학교이름 확인o",
            }
        )

        # Then
        # self.assertEqual(result_glossary["trans_word"], "宇理 高校")
        self.assertEqual(glossary_response.status_code, 200)


        # 카테고리별 글로서리 조회
        # When
        glossary_by_category_response = self.client.get(
            f"/api/v1/projects/{project.pk}/glossaries", {"category":result_category["pk"]},
        )
        
        glossary_by_category_result = glossary_by_category_response.json()

        # Then
        self.assertEqual([i["trans_word"] for i in glossary_by_category_result][0],  "宇理 高校")

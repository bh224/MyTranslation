from urllib import response
from rest_framework.test import APITestCase
from projects.models import Project, Project_Member
from users.models import User

class TestProjectAPI(APITestCase):
    def user_logged_in(self, username, is_admin):
        user = User.objects.create(username=username, is_admin=is_admin)
        user.set_password("1234")
        user.save()
        self.client.force_login(user)
        return user
    
    def test_get_projects(self) -> None:
        # Given
        manager = self.user_logged_in("manager", True)
        # author = self.user_logged_in("author", False)
        # checker = self.user_logged_in("checker", False)

        [
            Project.objects.create(
                category="webtoon",
                title=f"title{i}",
                description= "한일/네이버웹툰",
                author=manager,
            )
            for i in range(1, 11)
        ]

        # When
        response = self.client.get(
            "/api/v1/projects/", {"page": 1},
        )

        result = response.json()

        # Then
        self.assertEqual(result[0]["title"], "title1")
        self.assertEqual(len(result), 10)


    def test_create_a_project(self) -> None:
        # Given
        manager = self.user_logged_in("manager", True)
        author = self.user_logged_in("author", False)
        checker = self.user_logged_in("checker", False)

        # When
        response = self.client.post(
            "/api/v1/projects/",
            data = {
                "category": "webtoon",
                "title": "여신강림",
                "description": "한일/네이버웹툰",
                "manager": manager.pk,
                "author": author.pk,
                "checker": checker.pk,
            }
        )

        result = response.json()
        project_pk = result["pk"]
        project = Project_Member.objects.filter(project=project_pk)

        # Then
        self.assertEqual(result["title"], "여신강림")
        self.assertEqual(len(project), 3)


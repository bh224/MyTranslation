from rest_framework.test import APITestCase
from projects.models import Project, Project_Member
from users.models import User

class TestProjectServices(APITestCase):
    def create_user(self, username, is_admin):
        user = User.objects.create(username=username, is_admin=is_admin)
        user.set_password("1234")
        user.save()
        return user
    
    def test_create_a_project(self) -> None:
        # Given
        manager = self.create_user("manager", True)
        author = self.create_user("author", False)
        checker = self.create_user("checker", False)

        project = Project.objects.create(category="webtoon", title="여신강림", description="한일/네이버웹툰/시즌1", uploader=manager)

        Project_Member.objects.create(project=project, member=manager, role="manager")
        Project_Member.objects.create(project=project, member=author, role="author")
        Project_Member.objects.create(project=project, member=checker, role="checker")

        # When
        members = project.members.all()
        title = author.projects.get().title
        role = Project_Member.objects.filter(project=project, member=checker).get().role

        # Then
        self.assertEqual(3, members.count())
        self.assertEqual("여신강림", title)
        self.assertEqual("checker", role)

    def test_edit_project_members(self) -> None:
        # Given
        manager = self.create_user("manager", True)
        author = self.create_user("author", False)
        checker = self.create_user("checker", False)

        project = Project.objects.create(category="webtoon", title="판타지", description="한일/웹툰/시즌1", uploader=manager)

        Project_Member.objects.create(project=project, member=manager, role="manager")
        Project_Member.objects.create(project=project, member=author, role="author")
        Project_Member.objects.create(project=project, member=checker, role="checker")

        # When
        deleted_cnt, _ = Project_Member.objects.filter(project=project, member=checker).delete()
        new_checker = self.create_user("new_checker", False)
        result2 = Project_Member.objects.create(project=project, member=new_checker, role="checker")
        members = project.members.all()
        
        # Then
        with self.assertRaises(Project_Member.DoesNotExist):
            Project_Member.objects.filter(project=project, member=checker).get()

        self.assertEqual(deleted_cnt, 1)
        self.assertEqual("new_checker", result2.member.username)
        self.assertEqual(members.count(), 3)




    




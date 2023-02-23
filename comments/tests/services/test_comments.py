from asyncore import write
from rest_framework.test import APITestCase
from comments.models import Comment
from comments.services.comment_service import get_comments_list
from projects.models import Project
from users.models import User

class TestComment(APITestCase):
    def test_create_a_comment(self) -> None:
        # Given
        user = User.objects.create(username="test_writer", password="1234")
        project = Project.objects.create(category="game", title="test_game", description="한일/모바일게임", uploader=user)

        # When
        comment = Comment.objects.create(project=project, writer=user, content="코멘트작성")

        # Then
        self.assertEqual(comment.content, "코멘트작성")

    def test_get_comments_list(self) -> None:
        # Given
        user = User.objects.create(username="test_user", password="1234")
        project = Project.objects.create(category="webtoon", title="웹툰번역", description="한일/네이버웹툰", uploader=user)
        comments = [Comment.objects.create(project=project, writer=user, content=f"코멘트{i}") for i in range(1, 11)]

        # When
        result_comment = get_comments_list(project.pk, 1)
        # result_comment = Comment.objects.order_by("-id").filter(project=project.pk)[0:5]

        # Then
        self.assertEqual([comment.pk for comment in reversed(comments[5:11])], [comment.pk for comment in result_comment])

    def test_edit_and_delete_a_comment(self) -> None:
        # Given
        user = User.objects.create(username="test_writer", password="1234")
        project = Project.objects.create(category="game", title="test_project", description="test_한일/모바일게임", uploader=user)
        comment = Comment.objects.create(project=project, writer=user, content="프로젝트 코멘트")

        # 코멘트수정
        # When
        edited_comment = Comment.objects.filter(pk=comment.pk).update(content="코멘트수정")
        result_comment = get_comments_list(project.pk, 1)

        # Then
        self.assertEqual(len(result_comment), 1)
        self.assertEqual([i.content for i in result_comment], ["코멘트수정"])

        # 코멘트삭제
        # When
        edited_comment = Comment.objects.filter(pk=comment.pk).get()
        edited_comment.delete()
        result_comment = get_comments_list(project.pk, 1)

        # Then
        self.assertEqual(len(result_comment), 0)




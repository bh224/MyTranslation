# from urllib import response
# from rest_framework.test import APITestCase
# import comments
# from projects.models import Project
# from comments.models import Comment
# from users.models import User

# class TestComment(APITestCase):
#     def user_logged_in(self, username, is_admin):
#         user = User.objects.create(username=username, is_admin=is_admin)
#         user.set_password("1234")
#         user.save()
#         self.client.force_login(user)
#         return user
    
#     def test_get_comments_list(self) -> None:
#         # Given
#         user = self.user_logged_in("test_user", True)
#         project =  Project.objects.create(
#                 category="webtoon",
#                 title="test_title",
#                 description= "한일/네이버웹툰",
#                 uploader=user,
#             )
#         [Comment.objects.create(project=project, writer=user, content=f"코멘트{i}") for i in range(1, 11)]

#         # When
#         response = self.client.get(
#             f"/api/v1/projects/{project.pk}/comments", {"page":1}
#         )
#         result = response.json()

#         # Then
#         self.assertEqual(len(result), 5)
    
#     def test_create_a_comment(self) -> None:
#         # Given
#         user = self.user_logged_in("test_user", True)
#         project =  Project.objects.create(
#                 category="test_webtoon",
#                 title="test_title",
#                 description= "한일/네이버웹툰",
#                 uploader=user,
#             )
        
#         # When
#         response = self.client.post(
#             f"/api/v1/projects/{project.pk}/comments",
#             data={
#                 "writer": user.pk,
#                 "content": "코멘트 작성 테스트",
#             }
#         )

#         result = response.json()

#         # Then
#         self.assertEqual(result["content"], "코멘트 작성 테스트")

#     def test_edit_and_delete_a_comment(self) -> None:
#         # Given
#         user = self.user_logged_in("test_user", True)
#         project =  Project.objects.create(
#                 category="test_webtoon",
#                 title="test_title",
#                 description= "한일/네이버웹툰",
#                 uploader=user,
#             )
#         comment = Comment.objects.create(project=project, writer=user, content="코멘트추가")

#         # When
#         response = self.client.put(
#             f"/api/v1/comments/{comment.pk}",
#             data={
#                 "writer": user.pk,
#                 "content": "코멘트수정"
#             }
#         )
#         result = response.json()

#         # Then
#         self.assertEqual(result["content"], "코멘트수정")

#         # 코멘트삭제
#         response = self.client.delete(
#             f"/api/v1/comments/{comment.pk}",
#         )

#         self.assertEqual(response.status_code, 204)


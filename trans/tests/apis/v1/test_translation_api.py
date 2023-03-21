# import json
# import openpyxl
# from rest_framework.test import APITestCase
# from trans.models import CheckTranslation, Translation
# from users.models import User
# from projects.models import Project


# class TestTranslationAPI(APITestCase):
#     def create_a_user(self, username, is_admin):
#         user = User.objects.create(username=username, is_admin=is_admin)
#         user.set_password("1234")
#         user.save()
#         self.client.force_login(user)
#         return user

#     def create_a_project(self, category, title, description, uploader):
#         project = Project.objects.create(
#             category=category, title=title, description=description, uploader=uploader
#         )
#         return project

#     def test_upload_raw_data_and_get_translation_data_api(self) -> None:
#         user = self.create_a_user("test_user10", False)
#         checker = self.create_a_user("test_checker10", False)
#         project = self.create_a_project("game", "songbird symphony", "jpn-> kor", user)
#         wb = openpyxl.load_workbook("test.xlsx")
#         ws = wb["Sheet1"]
#         # 데이터저장
#         for row in ws.iter_rows(min_row=2):
#             #빈셀 제거
#             if row[0].value == None and row[1].value == None:
#                 continue
#             translation = Translation.objects.create(project=project, num=row[0].value, remark=row[1].value, origin_data=row[2].value, author=user)
#             CheckTranslation.objects.create(project=project, translation=translation, checker=checker)

#         # When
#         response = self.client.get(
#             f"/api/v1/projects/{project.pk}/translations", {"next": 0},
#         )
#         result = response.json()
        
#         # Then
#         # self.assertEqual(len(result), 10) #limit 개수 수정할 것
#         self.assertEqual(result[0]["translation_data"]["pk"], result[0]["translation"])
#         # self.assertEqual(result[-1]["cursorId"], 0)

#     def test_test_put_translation_api(self) -> None:
#         # Given
#         user = self.create_a_user("test_user10", False)
#         checker = self.create_a_user("test_checker10", False)
#         project = self.create_a_project("game", "songbird symphony", "jpn-> kor", user)
#         # 번역&체크데이터
#         translation1 = Translation.objects.create(project=project, author=user, num="1", remark="특수문자는 전각으로", origin_data="피이 삼촌, 피이 삼촌!!!")
#         CheckTranslation.objects.create(project=project, translation=translation1, checker=checker)

#         translation2 = Translation.objects.create(project=project, author=user, num="2", remark="특수문자는 전각으로", origin_data="안녕?")
#         CheckTranslation.objects.create(project=project, translation=translation2, checker=checker)

#         # 번역데이터수정
#         # When 
#         values = {
#                 f"1": {
#                     "pk": translation1.pk, 
#                     "trans_data": "ピーおじさん, おはよ！！！", 
#                     "details": "글로서리"
#                     },
#                 f"2": {
#                     "pk": translation2.pk, 
#                     "trans_data": "ピーおじさん, おはよ！！！", 
#                     "details": "글로서리"
#                     }
#             }
        
#         response = self.client.put(
#             f"/api/v1/projects/{project.pk}/translations",
#             data= json.dumps(values),
#             content_type="application/json"
#         )

#         result_trans = response.json()

#         # Then
#         self.assertEqual(len(result_trans["results"]), 2)

#         # 체크데이터수정
#         #When
#         chk_values = {
#             f"{translation1.pk}": {
#                 "translation": translation1.pk, 
#                 "note": "특수문자 전각으로 바꿔주세요", 
#                 "is_checked": True
#                 },
#             f"{translation2.pk}": {
#                 "translation": translation2.pk, 
#                 "note": "", 
#                 "details": True
#                 }
#         }

#         response = self.client.put(
#             f"/api/v1/projects/{project.pk}/checks",
#             data= json.dumps(chk_values),
#             content_type="application/json"
#         )

#         result_check = response.json()

#         # Then
#         self.assertEqual(len(result_check["results"]), 2)
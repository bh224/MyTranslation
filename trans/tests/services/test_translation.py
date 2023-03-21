# import openpyxl
# from django.db import connection
# from rest_framework.test import APITestCase
# from django.test.utils import CaptureQueriesContext
# from trans.services.translation_service import get_translation_data_list
# from users.models import User
# from projects.models import Project
# from trans.models import Translation, CheckTranslation

# class TestTranslation(APITestCase):
#     def create_a_user(self, username, is_admin):
#         user = User.objects.create(
#             username=username, password="1234", is_admin=is_admin
#         )
#         return user
    
#     def create_a_project(self, category, title, description, uploader):
#         project = Project.objects.create(
#             category=category, title=title, description=description, uploader=uploader
#         )
#         return project
    
#     def test_upload_raw_data_and_get_translation_data(self) -> None:
#         # Given
#         user = self.create_a_user("test_user5", False)
#         checker = self.create_a_user("test_checker", False)
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

#         # 번역데이터 저장
#         # When
#         trans_data = Translation.objects.filter(project=project.pk)[0:10]
#         check_data = CheckTranslation.objects.filter(project=project.pk)[0:10]

#         # Then
#         self.assertEqual(len(trans_data), 10)
#         self.assertEqual(len(check_data), 10)
#         self.assertEqual([i.checker.username for i in check_data][0], "test_checker")

#         # 번역데이터 조회
#         # When
#         with CaptureQueriesContext(connection) as ctx:
#         # with self.assertNumQueries(1):
#             # check_data = CheckTranslation.objects.filter(project=project.pk)[0:10]
#             # trans_data = [i for i in check_data] #2
#             # result_trans = [i.translation.trans_data for i in trans_data] # 10
#             # check_data = CheckTranslation.objects.select_related("translation").filter(project=project.pk)[0:10]
#             check_data = get_translation_data_list(project.pk, 0)
#             result_data = [i.translation.trans_data for i in check_data] #1
#             # result_trans = [i.trans_data for i in result_data] #1


#             # Then
#             self.assertEqual(result_data[0], None)


#     def test_put_translation(self) -> None:
#         # Given
#         user = self.create_a_user("test_author", False)
#         checker = self.create_a_user("test_checker", False)
#         project = self.create_a_project("game", "songbird symphony", "jpn-> kor", user)
#         translation = Translation.objects.create(project=project, author=user, num="1", remark="특수문자는 전각으로", origin_data="피이 삼촌, 피이 삼촌!!!")
#         CheckTranslation.objects.create(project=project, translation=translation, checker=checker)

#         # When
#         Translation.objects.filter(pk=translation.pk).update(trans_data="ピーおじさん,おはよう！！！", details="글로서리에 캐릭터추가")
#         CheckTranslation.objects.filter(translation=translation.pk).update(note="ピーおじさん、おはよう！！！ *특수문자 변경", is_checked=True)

#         result_trans = Translation.objects.get(pk=translation.pk)
#         result_check = CheckTranslation.objects.get(translation=translation.pk)

#         # Then
#         self.assertEqual(result_trans.pk, result_check.translation_id)
#         self.assertEqual(result_trans.trans_data, "ピーおじさん,おはよう！！！")
#         self.assertEqual(result_check.is_checked, True)

#     def test_translation_data_pagination(self) -> None:
#         pass
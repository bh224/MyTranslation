from typing import List
import MySQLdb
from django.db.models import QuerySet
from rest_framework.response import Response
from rest_framework import status
from trans.models import CheckTranslation, Translation
from trans.serializers import PutTranslationSerializer, PutCheckTranslationSerializer

def get_translation_data_list(project_pk: int, next: int) -> QuerySet[CheckTranslation]:
    limit = 1

    # start = (page-1) * limit
    # end = start + limit
    # return CheckTranslation.objects.select_related("translation").filter(project=project_pk)[start:end]

    # 커서기반 페이징
    return CheckTranslation.objects.raw(
        f"SELECT * FROM trans_checktranslation LEFT OUTER JOIN trans_translation ON (trans_checktranslation.translation_id = trans_translation.id) WHERE trans_checktranslation.project_id = {project_pk} and trans_translation.id > {next} LIMIT {limit}"
    )

def put_translation_data(data) -> List[int]:
    updated_done = []
    for pk, data in data.items():
        translation_pk = int(pk)
        translation = Translation.objects.get(pk=translation_pk)
        serializer = PutTranslationSerializer(translation, data=data, partial=True)
        if serializer.is_valid():
            edited_trans = serializer.save()
            updated_done.append(edited_trans.pk)
        else: 
            return Response(serializer.errors)
    return updated_done

def put_check_data(data) -> List[int]:
    updated_done = []
    for pk, data in data.items():
        translation_pk = int(pk)
        check_translation = CheckTranslation.objects.get(translation=translation_pk)
        serializer = PutCheckTranslationSerializer(check_translation, data=data, partial=True)
        if serializer.is_valid():
            edited_check = serializer.save()
            updated_done.append(edited_check.pk)
        else: 
            return Response(serializer.errors)
    return updated_done
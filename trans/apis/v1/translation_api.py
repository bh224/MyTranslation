import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from trans.models import Translation, CheckTranslation
from trans.serializers import TranslationDataSerializer, PutTranslationSerializer, PutCheckTranslationSerializer
from trans.services.translation_service import get_translation_data_list, put_check_data, put_translation_data


class Translations(APIView):
    def get(self, request, pk):
        try:
            next = request.query_params.get("next", 0)
            next = int(next)
        except:
            next = 0
        print(next)
        data = get_translation_data_list(pk, next)
        serializer = TranslationDataSerializer(data, context={"request": request}, many=True)
        add_cursor_id = list(serializer.data)
        add_cursor_id.append({"cursorId": next+1})

        return Response(serializer.data)
    
    def put(self, request, pk):
        updated_done = put_translation_data(request.data)
        data = {"results": updated_done}
        return Response(data)
        

class Check(APIView):
    def put(self, request, pk):
        updated_done = put_check_data(request.data)
        data = {"results": updated_done}
        return Response(data)
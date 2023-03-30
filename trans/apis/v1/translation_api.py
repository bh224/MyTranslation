import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from trans.models import Translation, CheckTranslation
from trans.serializers import TranslationDataSerializer, PutTranslationSerializer, PutCheckTranslationSerializer
from trans.services.translation_service import get_translation_data_list, put_check_data, put_translation_data
from trans.tasks import send_email


class Translations(APIView):
    def get(self, request, pk):
        try:
            next = request.query_params.get("next", 0)
            next = int(next)
        except:
            next = 0
        # print(next)
        data = get_translation_data_list(pk, next)
        serializer = TranslationDataSerializer(data, context={"request": request}, many=True)
        add_cursor_id = list(serializer.data)
        add_cursor_id.append({"cursorId": next+1})
        return Response(serializer.data)
    
    # 번역데이터 수정
    def put(self, request, pk):
        updated_done = put_translation_data(request.data)
        data = {"results": updated_done}
        return Response(data)
        
# 체크데이터 수정
class Check(APIView):
    def put(self, request, pk):
        #print(request.data)
        updated_done = put_check_data(request.data)
        data = {"results": updated_done}
        all_is_checked = CheckTranslation.objects.filter(project_id=pk, is_checked=False)
        # is_checked 가 전부 True 인 경우 메일 발송
        if not all_is_checked:
            result = send_email.delay(pk)
        return Response(data)
    
class PapagoAPI(APIView):
    def post(self, request):
        text = request.data["text"]
        # print(text)
        client_id = "GYBy09vHv2hRgirRQlGR" 
        client_secret = "PQ8sIX4gu9" 
        data = {
            "source": "ko",
            "target": "ja",
            "text": text
        }
        response = requests.post(
            'https://openapi.naver.com/v1/papago/n2mt',
            data=data,
            headers={
                'X-Naver-Client-Id':client_id, 
                'X-Naver-Client-Secret': client_secret
            }
        )
        rescode = response.status_code
        if(rescode==200):
            response_body = response.json()
            # print(response_body)
            return Response({"detail": response_body["message"]["result"]["translatedText"]})
        else:
            print("Error Code:" + rescode)
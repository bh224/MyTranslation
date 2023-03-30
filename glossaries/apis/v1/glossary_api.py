import json
import MySQLdb
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from glossaries import serializers
from glossaries.models import Glossary, NameRecommend
from glossaries.serializers import GlossarySerializer
from glossaries.services.glossary_service import get_a_category, get_glossary_by_category
from projects.services.project_service import get_a_project
from namecrawling.tasks import scrap_names


class Glossaries(APIView):
    """ 글로서리 단어 등록 / 카테고리별 글로서리 조회 """
    def post(self, request, pk):
        project = get_a_project(pk)
        category = get_a_category(request.data["category_pk"])
        serializer = GlossarySerializer(data=request.data)
        if serializer.is_valid():
            glossary = serializer.save(
                project=project, 
                category=category, 
                author=request.user,
            )
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def get(self, request, pk):
        # 카테고리별 용어
        category = request.query_params.get("name")
        if category:
            glossaries = Glossary.objects.filter(project=pk, category=category)
            serializer = GlossarySerializer(glossaries, many=True)
            return Response(serializer.data)
        # 전체 용어
        else:
            glossaries = Glossary.objects.filter(project=pk).order_by("category")
            serializer = GlossarySerializer(glossaries, many=True)
            return Response(serializer.data)
        
class Marker(APIView):
    """ 글로서리 마커 """
    words_list = set()

    def morpheme(self, word):
        if len(word) <= 4:
            for i in range(len(word) - 1):  # 3-4글자인 경우
                Marker.words_list.add(word[i] + word[i + 1])
        else:  # 5글자 이상인 경우 앞에 세글자 부터
            for j in range(2, len(word)):
                Marker.words_list.add(word[0:j])

    def get(self, request, pk):
        # todo 배포시 db 환경설정 추가
        conn = MySQLdb.connect(read_default_file="my.cnf")
        cursor = conn.cursor()
        # todo 배포시 db 환경설정 추가
        query = f"SELECT gs.id, gs.origin_word FROM dev_mytranslation.glossaries_glossary as gs where gs.project_id={pk} order by gs.category_id;"

        cursor.execute(query)
        result = list(cursor.fetchall())

        for word in result:  # 단어 하나씩 가져오기
            Marker.words_list.add(word[1])  # 원본단어
            space = word[1].find(" ")  # 공백있는경우
            if space >= 0:
                for i in word[1].split():  # 공백으로 쪼개고 추가
                    Marker.words_list.add(i)
                merged_word = "".join(word[1].split())  # 공백 합치고 추가
                Marker.words_list.add(merged_word)
                self.morpheme(merged_word)
            else:
                self.morpheme(word[1])
        
        glassary_words = list(Marker.words_list)

        return Response(glassary_words)


# 이름 추천 /glossaries/recommend-names 
class RandomNames(APIView):
    def get(self, request):
        sex = request.query_params.get("sex")
        recommended_name = []
        for _ in range(5):
            name = NameRecommend.objects.filter(sex=sex).order_by('?')[0]
            name_kanji =  f"{name.last_name} {name.first_name}"
            name_furigana = name.furigana
            recommended_name.append({"name":name_kanji, "furigana": name_furigana})
        return Response({"details": recommended_name})

# 랜덤 이름 스크래핑 /glossaries/scrap-names
class ScrapNames(APIView):
    def get(self, request):
        # country = request.query_params.get("country", None)
        # sex = request.GET.get("sex", None)
        # os.system(f"scrapy crawl names -O randomname.json -a country={country} -a sex={sex}")
        # scrap_names.delay(country, sex)
        sex = ["male", "female"]
        for s in sex:
            scrap_names.delay(s)
        return Response("done")
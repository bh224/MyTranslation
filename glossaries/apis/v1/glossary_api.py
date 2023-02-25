from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from glossaries.serializers import GlossarySerializer
from glossaries.services.glossary_service import get_a_category
from projects.services import get_a_project


class Glossary(APIView):
    """ 글로서리 단어 등록 """
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
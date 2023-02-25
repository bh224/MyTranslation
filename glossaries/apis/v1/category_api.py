from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from projects.models import Project
from glossaries.serializers import CategorySerializer
from projects.services.project_service import get_a_project

class Category(APIView):
    """ 글로서리 카테고리 """
    def post(self, request, pk):
        project = get_a_project(pk)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save(project=project, author=request.user)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
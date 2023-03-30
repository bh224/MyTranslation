from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from glossaries.models import Category
from projects.models import Project
from glossaries.serializers import CategorySerializer
from projects.services.project_service import get_a_project

class Categories(APIView):
    """ 글로서리 카테고리 """
    def get(self, request, pk):
        categories = Category.objects.filter(project=pk)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        project = get_a_project(pk)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save(project=project, author=request.user)
            serializer = CategorySerializer(category)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
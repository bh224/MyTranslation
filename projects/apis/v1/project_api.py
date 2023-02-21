from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from projects.models import Project, Project_Member
from users.models import User


class Projects(APIView):
    """ 프로젝트 관련 """
    
    # 모든 프로젝트 불러오기
    def get(self, request):
        projects = Project.objects.all()
        # todo 페이지네이션
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    # 프로젝트 생성
    def post(self, request):
        manager_pk = request.data['manager']
        author_pk = request.data['author']
        checker_pk = request.data['checker']

        manager = User.objects.get(pk=manager_pk)
        author = User.objects.get(pk=author_pk)
        checker = User.objects.get(pk=checker_pk)

        serializer = ProjectDetailSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(author=manager)

            Project_Member.objects.create(project=project, member=manager, role="manager")
            Project_Member.objects.create(project=project, member=author, role="author")
            Project_Member.objects.create(project=project, member=checker, role="checker")
            
            serializer = ProjectListSerializer(project)
            return Response(serializer.data)
        return Response(serializer.errors)
            

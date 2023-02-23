from dataclasses import field
from rest_framework.serializers import ModelSerializer
from projects.models import Project, Project_Member
from users.serializers import UserSerializer

class ProjectListSerializer(ModelSerializer):
    """ 프로젝트 리스트 """

    class Meta:
        model = Project
        fields = (
            "pk",
            "category",
            "title",
            "description",
        )

class ProjectDetailSerializer(ModelSerializer):
    """ 프로젝트 상세 """
    author = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            "pk",
            "category",
            "title",
            "description",
            "members",
            "author",
        )

class ProjectMembersSerializer(ModelSerializer):
    """ 프로젝트 참여멤버 """

    member = UserSerializer(read_only=True)

    class Meta:
        model = Project_Member
        fields = (
            "project",
            "member",
            "role",
        )
from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from users.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
    """ 프로젝트 코멘트 """
    writer = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = (
            "pk",
            "writer",
            "content",
        )
        read_only_fields = ['project']
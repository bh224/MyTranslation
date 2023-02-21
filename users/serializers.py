from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from users.models import User

class UserSerializer(ModelSerializer):
    """ 유저정보 """
    class Meta:
        model = User
        fields = ("pk", "username", "email")
        
    
from os import stat
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer



class Users(APIView):
    """ 모든 유저조회, 유저 등록 """
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        code = request.data.get("code")
        token = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": settings.GG_CLIENT_ID,
                "client_secret": settings.GG_CLIENT_SECRET,
                "redirect_uri": settings.LOGIN_REDIRECT_URL,
                "grant_type": "authorization_code",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        token = token.json().get("access_token")
        user_data = requests.get(
            f"https://www.googleapis.com/oauth2/v2/userinfo?access_token={token}",
            headers={
                "Authorization": f"Bearer {token}",
            },
        )
        user_data = user_data.json()
        try:
            user = User.objects.get(email=user_data["email"])
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            user = User.objects.create(
                username=user_data["email"],
                email=user_data["email"]
            )
            user.set_unusable_password()
            user.save()
            login(request, user)
            return Response(status=status.HTTP_200_OK)

class UserDetail(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class LogOut(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    def post(self,request):
        data =request.data
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        password=data.get('password')

        user = User.objects.create_user(first_name,last_name,email,password)
        user = UserCreateSerializer(user)


        return Response(user.data,status=status.HTTP_201_CREATED)
 
class RetrieveUserView(APIView): 
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        pass
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class UserView(APIView):
    """
        View to the user model 
    """
    serializer_class = UserSerializer

    def get(self, request, format=None) -> None:
        """
        Return a list with all the users
        """
        emails = [user.email for user in User.objects.all()]
        
        return Response(emails)
    
    def post(self, request):
        pass
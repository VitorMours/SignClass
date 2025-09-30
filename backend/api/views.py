from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
        CustomTokenObtainPairSerializer,
        UserSerializer,
        UserGetSerializer,
        SignGetSerializer,
        SignSerializer,
        VideoSerializer
    )
from .models import Sign, Video

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserView(APIView):
    """
    View to the custom user model inside of the application
    """

    serializer_class = UserSerializer

    def get(self, request, format=None) -> Response:
        """
        Return a list with all the users
        """
        users = User.objects.all()
        serializer = UserGetSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        """
        Create a new user
        """
        data = request.data.copy()

        password = data.get("password")
        if not password:
            return Response(
                {"password": ["Esse campo é obrigatorio"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            try:
                new_user = User(
                    first_name=serializer.validated_data.get("first_name"),
                    last_name=serializer.validated_data.get("last_name"),
                    email=serializer.validated_data.get("email"),
                    is_staff=serializer.validated_data.get("is_staff"),
                    is_superuser=serializer.validated_data.get("is_superuser")
                )

                new_user.set_password(serializer.validated_data.get("password"))
                new_user.save()

                return Response(
                    {
                        "message": "Usuario criado com sucesso",
                        "user": UserSerializer(new_user).data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
                return Response(
                    {"error": "Error interno do servidor"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
        
class SignView(APIView):
    
    serializer_class = SignSerializer
    
    def get(self, request) -> Response:
        """
        Get all the signs and the signs data
        """
        signs = Sign.objects.all()
        serialized_data = SignGetSerializer(signs, many=True)
        return Response(serialized_data.data, status= status.HTTP_200_OK)
    
    
    def post(self, request, format=None) -> Response:
        """
        Creting a sign view
        """
        
        data = request.data.copy()
        
        serializer = SignSerializer(data=data, many=False)
        
        if serializer.is_valid():
            try: 
                new_sign = Sign(
                    name = serializer.validated_data.get("name"),
                    meaning = serializer.validated_data.get("meaning"),
                    hand_configuration = serializer.validated_data.get("hand_configuration"),
                    articulation_point = serializer.validated_data.get("articulation_point"),
                    movement = serializer.validated_data.get("movement"),
                    body_expression  = serializer.validated_data.get("body_expression"),
                    direction_and_orientation = serializer.validated_data.get("direction_and_orientation"),
                    
                )
                new_sign.save()
                
                return Response(
                    {"sign": SignSerializer(new_sign).data},
                    status=status.HTTP_201_CREATED
                )
                
            except Exception as e:
                return Response(
                    {"error":"Please pass valid data to the form"}, 
                    status = status.HTTP_400_BAD_REQUEST    
               )
                
        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
class VideoView(APIView):
    
    serializer_class = VideoSerializer
    
    def get(self, request, format=None) -> Response:
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    # TODO: Implementar o metodo post
    def post(self, request, format=None) -> Response:
        pass
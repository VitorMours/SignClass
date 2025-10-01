from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
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
        VideoGetSerializer,
        VideoSerializer
    )
from .models import Sign, Video
from . import utils

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
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = VideoSerializer
    
    def get(self, request, format=None) -> Response:
        """
        To get all the videos in the database
        """
        videos = Video.objects.all()
        serializer = VideoGetSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None) -> Response:
        """
        Creating user video
        """
        if "media" not in request.FILES:
            return Response(
                {"error": "Send the video file"},
                status=status.HTTP_400_BAD_REQUEST
            )

        video_file = request.FILES["media"]
        
        if not utils.verify_video_file_extension_is_ok(video_file):
            return Response(
                {"error": "Invalid video file format"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        video_filename = utils.save_video_file(video_file)
        if not video_filename:
            return Response(
                {"error": "Failed to save video file"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
                
        try:
            owner_id = request.data.get("owner")
            sign_id = request.data.get("sign")
            
            if owner_id:
                try:
                    owner = User.objects.get(id=owner_id)
                except User.DoesNotExist:
                    return Response(
                        {"error": "User not found"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                owner = request.user
            
            if sign_id:
                try:
                    sign = Sign.objects.get(id=sign_id)
                except Sign.DoesNotExist:
                    return Response(
                        {"error": "Sign not found"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                        {"error": "You need to pass a sign"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            new_video = Video(
                name=request.data.get("name"),
                owner=owner,
                media=video_filename,
                media_filename=video_filename,
                knowledge_sector=request.data.get("knowledge_sector"),
                sign=sign,
            )
            
            new_video.save()
            serialized_video = VideoSerializer(new_video)
            
            return Response(
                {
                    "message": "Upload de video feito com sucesso",
                    "video": serialized_video.data
                }, 
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response(
                {
                    "error": f"Please pass valid data to the form: {str(e)}"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )           

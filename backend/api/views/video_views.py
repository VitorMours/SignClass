from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import (
        VideoGetSerializer,
        VideoSerializer,
        UserVideosSerializer
    )
from ..models import Sign, Video
from .. import utils

User = get_user_model()
         
class VideoView(APIView):
    """
    Resource feito para pegar todos os vídeos possiveis 
    sem qualquer tipo de distinção entre eles    

    """
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = VideoSerializer
    
    def get(self, request, format=None) -> Response:
        """
        To get all the videos in the database and return as json
        """
        videos = Video.objects.all()
        serializer = VideoGetSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None) -> Response:
        """
        Creating user video entity in the database with the data in the request body
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


class UserVideosView(APIView):
    
    serializer_class = UserVideosSerializer

    def get(self) -> None:
        pass

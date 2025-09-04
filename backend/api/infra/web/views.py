from rest_framework import viewsets, views
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from api.infra.db.models import Individual, Video
from api.infra.web.serializers import UserSerializer, VideoSerializer


class AuthenticationView(views.APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self) -> None:
        pass 
    
    def post(self, request) -> None:
        email = request.data.get("email")
        password = request.data.get("password")
        if authenticate(email, password):
            return Response({}) # TODO: Tem que preencher isso daqui ainda


class UserViewSet(viewsets.ModelViewSet):
    """
    User data endpoints
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Individual.objects.all()
    serializer_class = UserSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    Video data endpoints
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class UserVideoViewSet(viewsets.ModelViewSet):
    """
    Videos em que pertencem a um determinado usuario em que devemos ter o id dele dentro da rota para acessar
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = VideoSerializer
    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        return Video.objects.filter(owner__id=user_id)
    
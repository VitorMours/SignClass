from rest_framework import viewsets, views

from api.infra.db.models import Individual, Video
from api.infra.web.serializers import UserSerializer, VideoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    User data endpoints
    """
    queryset = Individual.objects.all()
    serializer_class = UserSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    Video data endpoints
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class UserVideoViewSet(viewsets.ModelViewSet):
    """
    Videos em que pertencem a um determinado usuario em que devemos ter o id dele dentro da rota para acessar
    """
    serializer_class = VideoSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        return Video.objects.filter(owner__id=user_id)
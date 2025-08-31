from rest_framework import viewsets
from api.infra.db.models import Individual
from api.infra.web.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = Individual.objects.all()
    serializer_class = UserSerializer




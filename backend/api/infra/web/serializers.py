from rest_framework import serializers
from api.infra.db.models import Individual, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual 
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = "__all__"
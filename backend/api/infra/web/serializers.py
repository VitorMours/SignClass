from rest_framework import serializers
from api.infra.db.models import Individual


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual 
        fields = "__all__"

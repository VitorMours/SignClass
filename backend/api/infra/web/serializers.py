from rest_framework import serializers
from api.infra.db.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]
        read_only_fields = ["id"]
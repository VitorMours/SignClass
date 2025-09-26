from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"
    
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            "password": attrs.get("password")
        }
        if not all(credentials.values()):
            raise serializers.ValidationError("Email e senha são obrigatórios")

        
        user = authenticate(**credentials)
        
        if user is None:
            raise serializers.ValidationError("Usuário Inexistente")
        
        data = super().validate(attrs)
        data["user_id"] = user.id
        data["email"] = user.email
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
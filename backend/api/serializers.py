from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Sign, Video

User = get_user_model()

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
        data["status"] = "success"
        data["email"] = user.email
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password","is_staff", "is_superuser"]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True}
        }

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id","first_name","last_name","email","is_staff","is_superuser"]
        
        
class SignGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign 
        fields = ["id","name","meaning","hand_configuration","articulation_point","movement","body_expression","direction_and_orientation","owner"]

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign 
        fields = ["name","meaning","hand_configuration","articulation_point","movement","body_expression","direction_and_orientation", "owner"]
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = ["name","owner","media","knowledge_sector","sign"]
        read_only_fields = ["media_filename"]

class VideoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = ["id","name","owner","media","knowledge_sector","sign"]
    
class UserVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = ["id","name","media","knowledge_sector","sign"]



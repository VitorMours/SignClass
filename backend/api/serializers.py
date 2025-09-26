from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate

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
        data["user_id"] = user.id
        data["email"] = user.email
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password","is_staff", "is_superuser"]
        
        
# FIXME: Precisa ser dois serializer, um para quando ler os dados e um para quando enviar os dados

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id","first_name","last_name","email","is_staff","is_superuser"]
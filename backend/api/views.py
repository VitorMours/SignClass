from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, UserGetSerializer

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserView(APIView):
    """
    View to the custom user model inside of the application
    """

    serializer_class = UserSerializer

    def get(self, request, format=None) -> Response:
        """
        Return a list with all the users
        """
        users = User.objects.all()
        serializer = UserGetSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data.copy()

        password = data.get("password")
        if not password:
            return Response(
                {"password": ["Esse campo é obrigatorio"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            try:
                new_user = User(
                    first_name=serializer.validated_data.get("first_name"),
                    last_name=serializer.validated_data.get("last_name"),
                    email=serializer.validated_data.get("email"),
                )

                new_user.set_password(serializer.validated_data.get("password"))

                new_user.save()

                return Response(
                    {
                        "message": "Usuario criado com sucesso",
                        "user": UserSerializer(new_user).data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
                return Response(
                    {"error": "Error interno do servidor"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
        
# class SignView()

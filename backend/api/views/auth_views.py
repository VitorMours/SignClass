from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers import CustomTokenObtainPairSerializer, UserSerializer

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # Para erros de validação, retorna 400 em vez de 401
            return Response(
                {
                    "detail": "Não foi possível fazer login com as credenciais fornecidas.",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Login bem-sucedido - retorna 200
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class SignUpView(APIView):
    """
        Visualização específica para signup 
        de usuarios por meio da rota 
        api/auth/signup
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None) -> Response:
        """
        Com esse método, é possível receber os dados 
        de dentro do request, e a partir deles conseguir 
        criar um usuário dentro do banco de dados
        
        """

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
                    is_staff=serializer.validated_data.get("is_staff", False),
                    is_superuser=serializer.validated_data.get("is_superuser", False)
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
                    {
                        "error": "Error interno do servidor",
                        "message":str(e)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
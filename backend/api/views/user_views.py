from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import (
        UserSerializer,
        UserGetSerializer,
    )

User = get_user_model()
    

class UserView(APIView):
    """
    View to the custom user model inside of the application, can be used to the CRUD basic actions of the resource in the database, can also be used to filtering necessities of the user in 
    the database
    """

    serializer_class = UserSerializer

    def get(self, request, format=None) -> Response:
        """
        Return a list with all the users or a list 
        with the users that can pass the query parameters
        filter properties
        
        Args:
        -----
                
        Returns:
        --------
        """
        try:
            if len(self.request.query_params) == 0:
                users = User.objects.all()
                
            else:
                filter_conditions = {}
                email = self.request.query_params.get("email", "")
                first_name = self.request.query_params.get("first_name", "")
                last_name = self.request.query_params.get("last_name", "")
                if email:
                    filter_conditions["email__icontains"] = email
                if first_name:
                    filter_conditions["first_name__icontains"] = first_name
                if last_name:
                    filter_conditions["last_name__icontains"] = last_name

                users = User.objects.filter(**filter_conditions)      

            serializer = UserGetSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {
                    "message":"Houve um erro durante o request",
                    "error":f"{str(e)}"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=False, permission_classes=[IsAdminUser])
    def post(self, request, format=None):
        """
        Create a new user
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
                    is_staff=serializer.validated_data.get("is_staff"),
                    is_superuser=serializer.validated_data.get("is_superuser")
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
        
class UserDetailView(APIView):
    
    serializer_class = UserGetSerializer
    
    def get(self, request, pk, format=None) -> Response:
        """
        Getting a specific user by the id specified in the url
        """
        try: 
            user = User.objects.get(id=pk)
            serialized = UserGetSerializer(user, many=False)

            return Response(
                {
                    "message":"User Founded",
                    "user":serialized.data
                }, 
                status=status.HTTP_302_FOUND) 
        except:
            return Response(
                {"message":"User Not Found"}, 
                status=status.HTTP_404_NOT_FOUND
                )
        
    
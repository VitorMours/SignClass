from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.infra.db.repositories import UserRepository
from api.core.usecases.user_usecase import UserUseCase
from api.infra.web.serializers import UserSerializer

class UserView(APIView):

    def get(self, request):
        repository = UserRepository()
        users = repository.get_all()  # retorna User
        serialized_data = UserSerializer(users, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        repository = UserRepository()
        use_case = UserUseCase(repository=repository)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user_entity = use_case.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        output_serializer = UserSerializer(user_entity)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

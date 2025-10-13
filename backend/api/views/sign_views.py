from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import ( SignGetSerializer, SignSerializer )
from ..models import Sign

User = get_user_model()
    
class SignView(APIView):
    
    serializer_class = SignSerializer
    
    def get(self, request, format=None) -> Response:
        """
        Get all the signs in the database and list them as json
        """
        signs = Sign.objects.all()
        serialized_data = SignGetSerializer(signs, many=True)
        return Response(serialized_data.data, status= status.HTTP_200_OK)
    
    
    def post(self, request, format=None) -> Response:
        """
        Create a sign object with the data provided in the request body
        """
        
        data = request.data.copy()
        
        serializer = SignSerializer(data=data, many=False)
        
        if serializer.is_valid():
            try: 
                new_sign = Sign(
                    name = serializer.validated_data.get("name"),
                    meaning = serializer.validated_data.get("meaning"),
                    hand_configuration = serializer.validated_data.get("hand_configuration"),
                    articulation_point = serializer.validated_data.get("articulation_point"),
                    movement = serializer.validated_data.get("movement"),
                    body_expression  = serializer.validated_data.get("body_expression"),
                    direction_and_orientation = serializer.validated_data.get("direction_and_orientation"),
                    
                )
                new_sign.save()
                
                return Response(
                    {"sign": SignSerializer(new_sign).data},
                    status=status.HTTP_201_CREATED
                )
                
            except Exception as e:
                return Response(
                    {"error":"Please pass valid data to the form"}, 
                    status = status.HTTP_400_BAD_REQUEST    
               )
                
        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
        # TODO: Adicionar visualziacoes relacionadas a detalhes especificos, e querys por usuario
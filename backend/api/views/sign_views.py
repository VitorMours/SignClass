from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from ..serializers import ( SignGetSerializer, SignSerializer )
from ..models import Sign
from django.db.models import Q

User = get_user_model()
    
class SignView(APIView):
    serializer_class = SignSerializer
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self, request, format=None) -> Response:
        """
        Get all signs or search signs by name/meaning
        """
        try:
            query = request.GET.get("q", "").strip()
            
            if query:
                print(f"Search query: {query}")
                signs = Sign.objects.filter(
                    Q(name__icontains=query) | Q(meaning__icontains=query)
                )[:10]
                print(f"Found {len(signs)} signs")
                
                # Usando serializer para consistência
                serializer = SignGetSerializer(signs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
                
            else:
                # Retorna todos os sinais (considerar paginação)
                signs = Sign.objects.all()
                serializer = SignGetSerializer(signs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error in SignView: {str(e)}")
            return Response(
                {"error": "Error searching for signs"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )        
    
    def post(self, request, format=None) -> Response:
        """
        Create a sign object with the data provided in the request body
        """
        
        data = request.data.copy()
        print(data) 
        serializer = SignSerializer(data=data, many=False)
        
        if serializer.is_valid():
            try: 
                owner_id = request.data.get("owner")
                
                if owner_id:
                    try:
                        owner = User.objects.get(id=owner_id)
                    except User.DoesNotExist:
                        return Response(
                            {"error": "User not found"}, 
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    owner = request.user
                
                new_sign = Sign(
                    name = serializer.validated_data.get("name"),
                    meaning = serializer.validated_data.get("meaning"),
                    hand_configuration = serializer.validated_data.get("hand_configuration"),
                    articulation_point = serializer.validated_data.get("articulation_point"),
                    movement = serializer.validated_data.get("movement"),
                    body_expression  = serializer.validated_data.get("body_expression"),
                    direction_and_orientation = serializer.validated_data.get("direction_and_orientation"),
                   owner = serializer.validated_data.get("owner") 
                )
                new_sign.save()
                
                return Response(
                    {"sign": SignSerializer(new_sign).data},
                    status=status.HTTP_201_CREATED
                )
                
            except Exception as e:
                return Response(
                    {"error":f"Please pass valid data to the form:{serializer.errors}"}, 
                    status = status.HTTP_400_BAD_REQUEST    
               )
                
        return Response(
            {"message": "Dados inválidos", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserSignDetailedView(APIView):
        
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self, request, pk, format=None) -> Response:
        try:
            user = User.objects.get(id=pk)
            signs = Sign.objects.filter(user=user)
            serialized = SignGetSerializer(signs, many=True)
            return Response(
                {
                    "message":"Signs Founded",
                    "signs":serialized.data
                }, 
                status=status.HTTP_200_OK
            )
            
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

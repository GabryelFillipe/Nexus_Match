from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Lobby
from players.models import Player
from .serializers import LobbySerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def lobby_list_create_view(request):
    
    if (request.method == 'GET'):
        lobbies = Lobby.objects.all()
        serializer = LobbySerializer(lobbies, many=True)
        return Response(serializer.data)
    
    if (request.method == 'POST'):

        try:
            player_profile = Player.objects.get(user=request.user)
        except Player.DoesNotExist:
            return Response(
                {"detail": "Você precisa criar um perfil de Jogador antes de criar salas."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = LobbySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(host=player_profile) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def player_lobby_join(request, pk):
    lobby = Lobby.get_object_or_404(pk= pk)
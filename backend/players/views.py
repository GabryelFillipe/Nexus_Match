from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Player
from .serializers import PlayerSerializer

@api_view(['GET'])
def get_all_players(request):
    players = Player.objects.all()
    
    
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_player_by_id(request, pk):
    player = get_object_or_404(Player, pk=pk)
    
    serializer = PlayerSerializer(player)
    return Response(serializer.data)
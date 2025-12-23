from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Game
from .serializers import GameSerializer

@api_view(['GET'])
def get_all_games(request):
    games = Game.objects.all()
    
    if 'genre' in request.query_params:
        genre_name = request.query_params['genre']
        games = games.filter(genres__name__icontains=genre_name)
        
    if 'platform' in request.query_params:
        platform_name = request.query_params['platform']
        games = games.filter(platforms__name__icontains=platform_name)

    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_game_by_id(request, pk):
    game = get_object_or_404(Game, pk=pk)
    
    serializer = GameSerializer(game)
    return Response(serializer.data)
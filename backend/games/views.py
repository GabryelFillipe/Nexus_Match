from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GameSerializer
from .models import Game, Genre, Platform


@api_view(['GET'])
def get_all_games(request):
    try:
        games = Game.objects.all()

        if 'genre' in request.query_params:
            genre_name = request.query_params['genre']

        # O __icontains busca pedaços do texto (ex: "Act" acha "Action")
            games = games.filter(genres__name__icontains=genre_name)

        if 'platform' in request.query_params:
            platform_name = request.query_params['platform']
            games = games.filter(platforms__name__icontains=platform_name)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    except Game.DoesNotExist:
        # Se não achar, retorna erro 404
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_game_by_id(request, pk):
    try:
        game = Game.objects.get(pk=pk)

        serializer = GameSerializer(game)
        return Response(serializer.data)

    except Game.DoesNotExist:
        # Se não achar, retorna erro 404
        return Response(status=status.HTTP_404_NOT_FOUND)

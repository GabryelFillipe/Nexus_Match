from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Player
from .serializers import PlayerSerializer
from games.models import Rank


@api_view(['GET'])
def get_all_players(request):
    players = Player.objects.all()

    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def player_detail_view(request, pk):
    player = get_object_or_404(Player, pk=pk)

    # Verifica se é um get, e se for lista o Player
    if (request.method== 'GET'):
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    # Verifica se é um PUT, e se for atualiza os dados do Player
    if (request.method == 'PUT'):
        # Atualiza os dados no banco
        serializer = PlayerSerializer(player, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if (request.method == 'DELETE'):
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

@api_view(['POST'])
def register_player(request):
    data = request.data

    # Verifica se username ou nickname já existem
    if User.objects.filter(username=data.get('username')).exists():
        return Response({"detail": "Este nome de usuário já está em uso."}, status=400)
        
    if Player.objects.filter(nickname=data.get('nickname')).exists():
        return Response({"detail": "Este nickname de jogador já está em uso."}, status=400)
    
    try:

        new_user = User.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email')
            )
        
        new_player = Player.objects.create(
            user=new_user,
            nickname=data.get('nickname'),
            discord_id=data.get('discord_id'),
            bio=data.get('bio', '') 
        )
        serializer = PlayerSerializer(new_player)
        return Response(serializer.data, status = 201)

    except Exception as e:
        return Response({"detail": str(e)}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_player_rank(request):
    rank_id = request.data.get('rank_id')
    if not rank_id:
        return Response({"detail": "O ID do rank é obrigatório."}, status=400)

    rank_novo = get_object_or_404(Rank, pk=rank_id)
    player = get_object_or_404(Player, user=request.user)

    
    rank_antigo = player.ranks.filter(game=rank_novo.game).first()
    
    if rank_antigo:
        player.ranks.remove(rank_antigo)
    
    player.ranks.add(rank_novo)
    

    return Response(
        {"detail": f"Rank {rank_novo.nome} definido para o jogo {rank_novo.game.nome}!"}, 
        status=status.HTTP_200_OK
    )
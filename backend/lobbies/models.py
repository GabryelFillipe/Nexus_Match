from django.db import models
from games.models import Game
from players.models import Player

class Lobby(models.Model):
    host = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='minhas_salas')
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='lobbies')
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    
    max_players = models.IntegerField(default=5)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    players = models.ManyToManyField(Player, related_name='salas_que_estou', blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.game.nome})"
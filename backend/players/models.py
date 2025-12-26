from django.db import models
from django.contrib.auth.models import User
from games.models import Rank

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    discord_id = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar_players', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    ranks = models.ManyToManyField(Rank, blank=True, related_name='players')

    def __str__(self):
        return self.nickname
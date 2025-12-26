from django.db import models

# Create your models here.



class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Game(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    data_lancamento = models.DateField()
    descricao = models.TextField()
    status = models.BooleanField(default=True)
    capa = models.ImageField(upload_to='capa_games', blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    
    platforms = models.ManyToManyField(Platform)
    
    def __str__(self):
        return self.nome
    
class Rank(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ranks')
    nome = models.CharField(max_length=50)
    ordem = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} - {self.game.nome}"
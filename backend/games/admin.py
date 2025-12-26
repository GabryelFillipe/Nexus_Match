from django.contrib import admin
from .models import Game, Genre, Platform, Rank  

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Rank)

# Register your models here.

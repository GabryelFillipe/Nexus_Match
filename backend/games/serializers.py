from rest_framework import serializers
from .models import Game, Genre, Platform


class GameSerializer(serializers.ModelSerializer):

    # Convente os IDs em nomes das plataformas e generos
    genres = serializers.StringRelatedField(many=True)
    platforms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Game
        fields = '__all__'

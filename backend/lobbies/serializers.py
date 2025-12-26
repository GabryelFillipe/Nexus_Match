from rest_framework import serializers
from .models import Lobby

class LobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Lobby
        fields = '__all__'
        read_only_fields = ['host']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['game'] = instance.game.nome 
        
        representation['host'] = instance.host.nickname 

        representation['players'] = [player.nickname for player in instance.players.all()]
        
        return representation
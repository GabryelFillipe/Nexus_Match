from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ['user', 'ranks']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['ranks'] = [
            f"{rank.game.nome}: {rank.nome}" 
            for rank in instance.ranks.all()
        ]
        
        return representation
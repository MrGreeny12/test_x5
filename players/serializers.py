from rest_framework import serializers
from players.models import Player, Club


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"
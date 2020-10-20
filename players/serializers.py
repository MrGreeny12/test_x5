from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    club_id = serializers.IntegerField()

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.club_id = validated_data.get('club_id', instance.club_id)
        instance.save()
        return instance

    class Meta:
        model = Player
        fields = ('name', 'club')
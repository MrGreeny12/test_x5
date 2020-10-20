from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
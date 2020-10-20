from rest_framework.response import Response
from rest_framework.views import APIView
from players.models import Player
from players.serializers import PlayerSerializer


class PlayerView(APIView):

    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response({"players": serializer.data})
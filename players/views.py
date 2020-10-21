from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from players.models import Player, Club
from players.serializers import PlayerSerializer, ClubSerializer


# class PlayerView(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Player.objects.all()
#         serializer = PlayerSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Player.objects.all()
#         player = get_object_or_404(queryset, pk=pk)
#         serializer = PlayerSerializer(player)
#         return Response(serializer.data)


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()






# class PlayerView(APIView):
#     '''
#     набор функций для работы с моделью игрока посредством API
#     '''
#     def get(self, request):
#         players = Player.objects.all()
#         serializer = PlayerSerializer(players, many=True)
#         return Response({"players": serializer.data})
#
#     def post(self, request):
#         player = request.data.get('players')
#         serializer = PlayerSerializer(data=player)
#         if serializer.is_valid(raise_exception=True):
#             player_saved = serializer.save()
#         return Response({"success": "Player '{}' created successfully".format(player_saved.name)})
#
#     def put(self, request, player_id):
#         saved_player = get_object_or_404(Player.objects.all(), pk=player_id)
#         data = request.data.get('players')
#         serializer = PlayerSerializer(instance=saved_player, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             player_saved = serializer.save()
#         return Response({
#             "success": "Player '{}' updated successfully".format(player_saved.name)
#         })
#
#     def delete(self, request, player_id):
#         player = get_object_or_404(Player.objects.all(), pk=player_id)
#         player.delete()
#         return Response({
#             "message": "Player with id `{}` has been deleted.".format(player_id)
#         }, status=200)
from django.test import TestCase
from .models import Player


class PuppyTest(TestCase):
    '''
    Тестирование модели Player
    '''
    def setUp(self):
        Player.objects.create(
            name='Lucas Moura', club=1)
        Player.objects.create(
            name='Gareth Bale', club=1)

    def test_player_club(self):
        player_lucas_moura = Player.objects.get(name='Lucas Moura')
        player_gareth_bale = Player.objects.get(name='Gareth Bale')
        self.assertEqual(
            player_lucas_moura.get_club(), "Lucas playing in Tottenham Hotspur.")
        self.assertEqual(
            player_gareth_bale.get_club(), "Gareth playing in Tottenham Hotspur.")
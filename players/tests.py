from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from players import views


class TestPlayers(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PlayerViewSet.as_view({'get': 'list'})
        self.uri = '/players/'

    def test_get_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        params = {
            "name": "test",
            "club_id": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))


class TestPlayer(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PlayerViewSet.as_view({'get': 'retrieve'})
        self.uri = '/players/<int:pk>'

    def test_get_retrieve(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_put_retrieve(self):
        params = {
            'name': 'Test test',
            'club_id': 2
        }
        request = self.factory.put(path=self.uri, data=params)
        response = self.view(request)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_delete_retrieve(self):
        request = self.factory.delete(path=self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
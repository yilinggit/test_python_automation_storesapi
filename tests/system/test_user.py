from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                ## This is not actually getting sent as json data, its getting sent as form data
                request = client.post('/register', data = {'username': 'jose',
                                                          'password': 'asdf'})

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('jose'))
                self.assertDictEqual({'message': "User created"},
                                     json.loads(request.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'jose', 'password': 'asdf'})

                ## data here needs to be sent as json, not form data. json.dumps converts to json-valid string
                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'jose', 'password': 'asdf'}),
                                           headers={'Content-Type': 'application/json'})

                ## check that access_token string is in what is returns
                self.assertIn('access_token', json.loads(auth_response.data).keys())




    def test_register_duplicate_users(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'jose', 'password': 'asdf'})
                response = client.post('/register', data={'username': 'jose', 'password': 'asdf'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': " a user with that username already exists"},
                                     json.loads(response.data))






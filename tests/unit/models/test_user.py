from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('testuser','testpassword')

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')
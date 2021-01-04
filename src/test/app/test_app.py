from src.test import db_testcase
from src.app import app
from werkzeug.security import check_password_hash


class TestAuth(db_testcase.DbTestCase):

    def test_load_user(self):
        user_1 = self.create_user()
        user_2 = self.create_user()
        loaded_user_1 = app.load_user(user_1['id'])
        loaded_user_2 = app.load_user(user_2['id'])

        self.assert_user(user_1, loaded_user_1)
        self.assert_user(user_2, loaded_user_2)

    def assert_user(self, expected_user, loaded_user):
        self.assertEqual(expected_user['id'], loaded_user.id)
        self.assertEqual(expected_user['name'], loaded_user.name)
        self.assertEqual(expected_user['email'], loaded_user.email)
        self.assertTrue(check_password_hash(loaded_user.password, expected_user['password']))

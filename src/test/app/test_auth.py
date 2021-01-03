from src.test import db_testcase
from src.app.app import app


class TestAuth(db_testcase.DbTestCase):

    def test_login_should_login(self):
        user = self.create_user()
        client = app.test_client()
        form = {
            'email': user['email'],
            'password': user['password']
        }

        client.post('/login', data=form)
        self.assert_flash_message(client, 'Bem-vindo, ' + user['name'])

    def test_login_user_does_not_exist(self):
        client = app.test_client()
        form = {
            'email': 'ronaldinho@gmail.com',
            'password': 'rolezinho'
        }

        client.post('/login', data=form)
        self.assert_flash_message(client, 'Usuário não cadastrado')

    def test_login_wrong_password(self):
        user = self.create_user()
        client = app.test_client()
        form = {
            'email': user['email'],
            'password': 'meu_cajado_azul'
        }

        client.post('/login', data=form)
        self.assert_flash_message(client, 'Senha inválida')

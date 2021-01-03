from src.test import db_testcase
from src.app.app import app
from src.app.lib.utils import dbutils


class TestAuth(db_testcase.DbTestCase):

    def test_signup_and_login(self):
        client = app.test_client()
        user = 'kikinho123'
        email = 'kiko_loureiro@megadeth.com'
        password = 'mustaine_eh_doido'
        form = {
            'user': user,
            'email': email,
            'password': password
        }

        client.post('/signup', data=form)

        form = {
            'email': email,
            'password': password
        }

        client.post('/login', data=form)
        self.assert_flash_message(client, 'Bem-vindo, ' + user)
        self.assert_user_logged_in(client, self.get_user_id(email))

    def test_signup_with_already_registered_user(self):
        existent_user = self.create_user()
        client = app.test_client()
        form = {
            'user': existent_user['name'],
            'email': existent_user['email'],
            'password': existent_user['password']
        }

        client.post('/signup', data=form)
        self.assert_flash_message(client, 'Email já cadastrado.')

    def test_signup_should_signup(self):
        client = app.test_client()
        user = 'kikinho123'
        email = 'kiko_loureiro@megadeth.com'
        password = 'mustaine_eh_doido'
        form = {
            'user': user,
            'email': email,
            'password': password
        }

        client.post('/signup', data=form)
        self.assert_flash_message(client, 'Cadastro realizado com sucesso. Bem-vindo, ' + user)

    def test_login_should_login(self):
        user = self.create_user()
        client = app.test_client()
        form = {
            'email': user['email'],
            'password': user['password']
        }

        client.post('/login', data=form)
        self.assert_flash_message(client, 'Bem-vindo, ' + user['name'])
        self.assert_user_logged_in(client, user['id'])

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

    def get_user_id(self, email):
        data = dbutils.execute_query('SELECT id FROM Users WHERE email = %s;', (email,))
        return data[0]['id']

    def assert_user_logged_in(self, client, user_id):
        with client.session_transaction() as session:
            self.assertEqual(user_id, int(session['_user_id']))

import sys
import os.path
sys.path.append(os.path.abspath('./'))

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.app.web.auth import auth
from src.app.web.main import main
from src.app.web.models import User
from src.app.lib.utils import dbutils
from src.app.lib.db.dbconnection import DbConnection

app = Flask(__name__, template_folder='web/templates')

#settings
app.secret_key = 'mysecretkey'

app.register_blueprint(auth)
app.register_blueprint(main)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Faça login para acessar esta página"
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DbConnection.get_main_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
	data = dbutils.execute_query('SELECT * FROM Users WHERE id = %s;', (user_id,))
	if data:
		return User(data[0]['id'], data[0]['name'], data[0]['email'], data[0]['password'])

	return None

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from typing import List, Dict
from flask_login import LoginManager
from web.auth import auth
from web.main import main
from web.models import User
import mysql.connector
import json
import uuid

app = Flask(__name__, template_folder='web/templates')

#MYSQL CONNECTION
config = {
	'user': 'root',
	'password': 'root',
	'host': 'mysql',
	'port': '3306',
	'database': 'Cah'
}

#settings
app.secret_key = 'mysecretkey'

app.register_blueprint(auth)
app.register_blueprint(main)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Faça login para acessar esta página"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Users WHERE id = %s', (user_id,))
	data = cursor.fetchall()
	if data:
		#vamos evitar magic numbers, por favor
		return User(data[0][0], data[0][1], data[0][2], data[0][3])
	else:
		return None


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)




##UNUSED METHODS##
# @app.route('/getUsers')
# def get_contacts():
# 	return json.dumps({'usuarios': getUsers()})

# @app.route('/delete/<string:id>')
# def delete_contact(id):
# 	connection = mysql.connector.connect(**config)
# 	cursor = connection.cursor()
# 	cursor.execute('DELETE FROM Users WHERE ID = {0}'.format(id))
# 	connection.commit()
# 	flash('Contato removido')
# 	return redirect(url_for('Index'))

# @app.route('/edit/<id>')
# def edit_contact(id):
# 	connection = mysql.connector.connect(**config)
# 	cursor = connection.cursor()
# 	cursor.execute('SELECT * FROM Users WHERE ID = %s', (id,))
# 	data = cursor.fetchall()
# 	return render_template('edit-contact.html', user = data[0])

# @app.route('/update/<id>', methods = ['POST'])
# def update(id):
# 	if request.method == 'POST':
# 		name = request.form['name']
# 		connection = mysql.connector.connect(**config)
# 		cursor = connection.cursor()
# 		cursor.execute("""
# 			UPDATE Users
# 			SET name = %s
# 			WHERE ID = %s
# 		 """, (name, id))
# 		connection.commit()
# 	return redirect(url_for('Index'))

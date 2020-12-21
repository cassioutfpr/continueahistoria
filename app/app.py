from flask import Flask, render_template, request, redirect, url_for, flash
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

#MYSQL CONNECTION
config = {
	'user': 'root',
	'password': 'root',
	'host': 'db',
	'port': '3306',
	'database': 'Cah'
}

#settings
app.secret_key = 'mysecretkey'
numberOfUsers = 0

def getUsers() -> List[Dict]:
	global numberOfUsers
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Users')
	data = cursor.fetchall()
	#results = [{id: name} for (id, name) in cursor]
	numberOfUsers = len(data)
	cursor.close()
	connection.close()

	return data

@app.route('/')
def Index():
	print(getUsers())
	return render_template('index.html', users = getUsers())

@app.route('/login')
def Login():
	return render_template('login.html')

@app.route('/register')
def Register():
	return render_template('register.html')

@app.route('/add_user', methods=['POST'])
def add_user():
	if request.method == 'POST':
		flash('')
		return redirect(url_for('Register'))

@app.route('/add_contact', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		name = request.form['name']
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()
		cursor.execute('INSERT INTO Users (id, name) VALUES (%s, %s)', ( "18", name))
		connection.commit()
		flash('Contact Added succesfully')
		cursor.close()
		connection.close()
		return redirect(url_for('Index'))

@app.route('/getUsers')
def get_contacts():
	return json.dumps({'usuarios': getUsers()})

@app.route('/delete/<string:id>')
def delete_contact(id):
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('DELETE FROM Users WHERE ID = {0}'.format(id))
	connection.commit()
	flash('Contato removido')
	return redirect(url_for('Index'))

@app.route('/edit/<id>')
def edit_contact(id):
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Users WHERE ID = %s', (id,))
	data = cursor.fetchall()
	return render_template('edit-contact.html', user = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update(id):
	if request.method == 'POST':
		name = request.form['name']
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()
		cursor.execute("""
			UPDATE Users
			SET name = %s
			WHERE ID = %s
		 """, (name, id))
		connection.commit()
	return redirect(url_for('Index'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
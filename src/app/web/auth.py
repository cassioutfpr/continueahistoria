from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import uuid
import os

auth = Blueprint('auth', __name__)

config = {
	'user': 'root',
	'host': os.environ['MAIN_DB_HOST'],
	'port': '3306',
	'database': 'Cah'
}

@auth.route('/login')
def login():
	return render_template('login.html')

@auth.route('/login', methods=['POST'])
def loginPost():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password'] 

		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM Users WHERE email = %s', (email,))
		data = cursor.fetchall()

		if not data:
			flash('Credenciais erradas')
			return redirect(url_for('auth.login'))

		if not check_password_hash(data[0][3], password):
			flash('Credenciais erradas')
			return redirect(url_for('auth.login'))


		#vamos evitar magic numbers, por favor
		login_user(User(data[0][0], data[0][1], data[0][2], data[0][3]))

		return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
	return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signupPost():
	if request.method == 'POST':
		#TODO: check if password and confirm password are the same
		#return to front

		user = request.form['user']
		email = request.form['email']
		password = request.form['password']  #HASH IT FIRST
	
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()

		cursor.execute('SELECT * FROM Users WHERE email = %s', (email,))
		data = cursor.fetchall()

		if data:
			flash('Email já cadastrado.')
			return redirect(url_for('auth.signup'))

		hashed_password = generate_password_hash(password, method='sha256')
		cursor.execute('INSERT INTO Users (id, name, email, password) VALUES (%s, %s, %s, %s)', (str(uuid.uuid4().hex), user, email, hashed_password))
		
		connection.commit()
		flash('Cadastro realizado com sucesso')
		cursor.close()
		connection.close()
	

		return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))
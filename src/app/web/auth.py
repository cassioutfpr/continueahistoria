from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.urls import url_parse
from src.app.web.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from src.app.lib.utils import dbutils

auth = Blueprint('auth', __name__)


next_page = None

@auth.route('/login', methods=['GET', 'POST'])
def login():
	global next_page
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		data = dbutils.execute_query('SELECT * FROM Users WHERE email = %s', (email,))

		print(data)

		if not data:
			flash('Usuário não cadastrado')
			return redirect(url_for('auth.login'))

		if not check_password_hash(data[0]['password'], password):
			flash('Senha inválida')
			return redirect(url_for('auth.login'))

		login_user(User(data[0]['id'], data[0]['name'], data[0]['email'], data[0]['password']))

		if not next_page or not safeUrl.is_safe_url(next_page, request):
			next_page = url_for('main.index')
		return redirect(next_page)

	next_page = request.args.get('next')
	return render_template('login.html')


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
		password = request.form['password']
		confirmPassword = request.form['confirmPassword']
	
		data = dbutils.execute_query('SELECT * FROM Users WHERE email = %s;', (email,))

		if data:
			flash('Email já cadastrado.')
			return redirect(url_for('auth.signup'))

		if password != confirmPassword:
			flash('As senhas devem ser iguais.')	
			return redirect(url_for('auth.signup'))

		hashed_password = generate_password_hash(password, method='sha256')
		dbutils.execute_statement('INSERT INTO Users (name, email, password) VALUES (%s, %s, %s);', (user, email, hashed_password))
		
		return redirect(url_for('main.index'))


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/profile')
def profile():
	return render_template('profile.html')

@main.route('/write_story')
@login_required
def RenderWriteStory():
	return render_template('writeStory.html', name = current_user.name)
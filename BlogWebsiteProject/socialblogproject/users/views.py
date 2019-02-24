from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from socialblogproject import db
from socialblogproject.models import User, BlogPost
from socialblogproject.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from socialblogproject.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('core.index'))

@users.route('/register', methods = ['GET', 'POST'])
def register():

	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email=form.email.data,
					username = form.username.data,
					password = form.password.data
					)

		db.session.add(user)
		db.session.commit()
		flash('You have registered!')
		return redirect(url_for('users.login'))

	return render_template('register.html', form = form)

@users.route('/login', methods = ['GET', 'POST'])
def login():

	form = LoginForm()

	if form.validate_on_submit():

		user = User.query.filter_by(email=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:
			login_user(user)
			flash('You are logged in!')

			next = request.args.get('next')

			if next == None or not next[0] == '/':
				next = url_for('core.index')

			return redirect(next)
	return render_template('login.html', form= form)

@users.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
	form = UpdateUserForm()

	if form.validate_on_submit():
		if form.picture.data:
			username = current_user.username
			pic = add_profile_pic(form.picture.data, username)
			current_user.profile_image = pic

		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('User Acccount Updated!')
		return redirect(url_for('users.account'))

	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email

	profile_image = url_for('static', filename = 'profile_pics/' + current_user.profile_image)

	return render_template('account.html', profile_image = profile_image, form = form)

@users.route('/<username>')
def user_posts(username):
	page = request.args.get('page', 1, type = int)
	user = User.query.filter_by(username = username).first_or_404()
	blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page = page, per_page = 4)
	return render_template('user_blog_posts.html', blog_posts = blog_posts, user= user)

@users.route('/list_of_users')
def list_of_users():
	# This method I use append all User attributes to a list. There may be an inbuilt function I do not know about.
	userlist = []
	count = 1
	while User.query.filter_by(id=count).first() is not None:
		userlist.append(User.query.filter_by(id = count).first())
		count += 1
	
	return render_template('list_of_users.html', userlist = userlist)
from flask import render_template, request, Blueprint
from socialblogproject.models import BlogPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
	page = request.args.get('page', 1, type=int)
	blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=10)
	return render_template('index.html', blog_posts = blog_posts)

@core.route('/about')
def about(): 
	return render_template('about.html')

@core.route('/mountains')
def mountains():
	return render_template('mountains.html')

@core.route('/nature')
def nature():
	return render_template('nature.html')

@core.route('/animals')
def animals():
	return render_template('animals.html')
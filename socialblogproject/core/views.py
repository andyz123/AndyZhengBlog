from flask import render_template, request, Blueprint
from socialblogproject.models import BlogPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
	return render_template('index.html')

@core.route('/blog')
def blog():
	page = request.args.get('page', 1, type=int)
	blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
	return render_template('blog.html', blog_posts = blog_posts)

@core.route('/portfolio')
def about(): 
	return render_template('about.html')

@core.route('/technology')
def technology():
	return render_template('technology.html')

@core.route('/headphones')
def headphones():
	return render_template('headphones.html')

@core.route('/animals')
def animals():
	return render_template('animals.html')

@core.route('/nature')
def nature():
	return render_template('nature.html')

@core.route('/goat')
def goat():
	return render_template('goat.html')
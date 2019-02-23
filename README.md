# Introduction
This is a blog site developed using the Flask framework and deployed to Heroku under the domain http://andyzhengblog.herokuapp.com. You're able to create an account, post messages, upload a profile picture and more.
- You do not need (and I recommend you do not) to use a legitimate email address to register in order to test the site. It just has to pass the email check (something@something.com)

# Features
I'll try to list them all.
- You are able to create an account.
- You are able to create posts and others can see it.
- You are able to edit your own posts.
- You can see all posts made by a certain person.
- Each separate account has a picture. We provide a default one, but you may upload your own.
- You can click on the date published to see all posts made that day.
- You can change your username and email.
- You can see all users who registered for our site.
- You can see a slideshow of Mountain pictures.
- You can see a slideshow of Nature pictures.
- You can see a slideshow of Animal pictures.
- New posts are tagged with a NEW! badge.
- You can see a list of registered users. (There are 3 dummy accounts I made to test the site already) 
- Since the site is uploaded to Heroku, all data is resetted after 30 minutes of inactivity unfortunately.

# Tech Stack
- Python and the Flask framework.
- HTML, CSS (Bootstrap)
- SQLite

The site's back-end is written in Python with the aid of the Flask framework and SQLite to save user data into a database. The front-end templates were written using HTML and CSS to improve the site's look.

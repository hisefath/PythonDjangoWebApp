# PythonDjangoWebApp
A Full stack web development practice with python and Django


*I'm working on a Mac*
But to get started: 
1. I'm using python 3.7.0 & Django 2.1.7 in this repo
2. I also use pip as my package manager and start my project with
```
cd /Documents/Github/<repoName>
```
3. Then use 
```
django-admin startproject <projectName>
```
4. Gives a code skeleton that looks like:
```
.
├── djangoProject
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py 
```
   ###### __init__.py - empty file just to say that this is a python package
   ###### settings.py - settings and config (includes secret key, debug mode, app section, database settings, etc.)
   ###### urls.py - mapping url routes
   ###### wsgi.py - how the python web app communicates with the server
5. To start server, run
```
python manage.py runserver
```
   ###### Django is a web project, within in the web project could be multiple apps
   ###### example of an app could be a blog section, then a store section, etc.
   ###### apps are pretty much containable and shippable to other web projects, resuable
6. To start an app, run
```
python manage.py startapp <appName>
```
7. Gives a code skeleton that looks like:
```
.
├── README.md
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
	a. import modules such as: (inViews:[httpReponse, Render]) create a view
	b. make urls.py file in app and include (inUrls:[include])
	c. type out path pattern
	d. type out path pattern in web project urls.py file
	e. workflow:: add views for app-> update path patterns for app -> update webapp path patterns
8. Creating Templates in an app directory
###### instead of creating html for all views, we create <templates> sub-directory
###### inside of templates, new subdirectory in the name of our app (although redundant, makes things clear)
###### <whateverAppName> -> templates -> <whatverAppName> -> template.html
	a. views.py -> render your html pages based on request
	b. templates-> blog -> <filename>.html we can have base.html for repeat code
	c. import bootstrap and custom.css for every item post
	d. update routes based on what we click on navbar
	e. also created dummy data as 'context'
9. To create a super user for the Administrator page, run
```
ptyhon manage.py makemigrations
python manage.py runserver
python manage.py createsuperuser
```
	a. you can now login, in /admin page
	b. click users to see your users
	c. you can edit info, check current users/groups/etc. 
	d. django doesnt store your actual passwords, it automatically hashes them
10. Create models class in your models.py file in your app directory
	a. run python manage.py makemigrations
	b. this creates a 0001_intial.py file under migrations sub-directory
	c. to create this table in your database, run 
	```
	python manage.py sqlmigrate blog 0001
	python manage.py sqlmigrate <appName> <migrationNumber>
	``` 
	d. After you create model class and create your table, run the migrate command 
	```
	python manage.py migrate
	```
	e. Migrations are so useful bc they allow us to make changes to our databses even after its created and has existing data in the database
	f. if you wanted to query the database using these models, you can access the shell by running
	```
	python manage.py shell
	```
	g. example commands in the shell
	```
	from blog.models import Post
	from django.contrib.auth.models import User
	//query users table
	User.objects.all()
	User.objects.first()
	User.objects.filter(username='mastershefu') //or any other attribute
	//capture user object in variable
	user = User.objects.filter(username='mastershefu')
	//now you can take the variable and see all attributes of that user object
	user.id
	user.pk
	user = User.objects.get(id=1)
	//query posts 
	Post.objects.all()
	post_1 = Post(title = 'textbook 1', details = 'textbook for sale', price=40, author=user) //user must be declared beforehand
	//save your post object to your database
	post_1.save()
	//check if it saved by running
	Post.objects.all()
	//in order to get your post objects to show up in a more descriptive form, use the dunder str method (dunder means double underscore)
	post = Post.objects.first() 
	post.details
	post.price
	post.author.email
	//query all posts made by a specific user
	.modelname_set
	user.post_set
	user.post_set.all() 
	user.post_set.create(title = 'textbook 3', details = 'textbook for sale', price=120) //automatically saves
	```
	h. go to app->views.py and replace dummy data with our post model
		- from .models import Post 
		- context -> posts -> Post.objects.all() 
		- to see the Post datatable in your /admin page, register it to your admin.py file in your app directory
		- import it again, then do admin.site.register(Post)

11. We have to create user registration, and we do this in a new app
```python manage.py startapp users```
	a. add to installed apps in settings.py file
	b. add function to views to render register user page
	c. add templates/users sub directory for html files
	d. create html file for view function
	e. update urls.py file 
	f. go back to views.py file, now if your form as a POST method, 
	your function should take the request and post it to the database.
	g. based on if the forms valid or not, we will both display success messages for the user and/or redirect them appropriately
	h. if you want messages to work, climb through your hierarchy and code for the success messages in your base.html template
	i. now that that works, you can save it to your database by adding form.save() in your register function in views.py
	j. To customize what fields you want users to register with, create new forms.py file in your users app directory, then import and use the class in made in views.py
	k. I'm using djangos "crispy-forms" to get a better styling
```pip install django-crispy-forms```
		- to use cripsy, list it in installed apps, dictacte which css framework youre using (both in settings.py file) then update your register.html file

12. We now have to create a login and logout system

	a. update urls.py with auth_views login & logout
	b. create login logout html files
	c. create redirect links after form submissions
	d. you can update your navbar for visual reinforcement of log in and log out actions
	e. workflow review: views.py in app -> create  function to render page -> update project's urls.py file, create the html in template/appname directory
	f. you can also restrict certain urls by making it so that we require an authentication/login before we access certain pages (for this you have to import decorators in your views.py file and update the link ur want redirection to in settings.py)

## How my file tree looks now
.
├── README.md
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── main.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    └── views.py

13. Creating user profiles and creating one to one relationship between users and profiles
	a. create model in models.py file in user app sub directory
	b. ```pip install Pillow```
	c. ```python manage.py makemigrations```
	d. ```python manage.py migrate```
	e. register profile model in admin.py
	f. run django shell 
	```
	python manage.py shell
	from django.contrib.auth.models import User
	user = User.objects.filter(username="mastershefu")
	user.profile
	user.profile.image
	user.profile.image.url
	```
	g. We have to direct which directory the images will be stored when we upload new pictures for every user, we do this in the settings.py file
	h. make a signal.py file so anytime we create a user, a profile is generated, and will be able to save the profile information 



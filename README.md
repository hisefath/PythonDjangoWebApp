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
	007. import modules such as: (inViews:[httpReponse, Render]) create a view
	107. make urls.py file in app and include (inUrls:[include])
	207. type out path pattern
	307. type out path pattern in web project urls.py file
	407. workflow:: add views for app-> update path patterns for app -> update webapp path patterns
8. Creating Templates in an app directory
###### instead of creating html for all views, we create <templates> sub-directory
###### inside of templates, new subdirectory in the name of our app (although redundant, makes things clear)
###### <whateverAppName> -> templates -> <whatverAppName> -> template.html
	008. views.py -> render your html pages based on request
	108. templates-> blog -> <filename>.html we can have base.html for repeat code
	208. import bootstrap and custom.css for every item post
	308. update routes based on what we click on navbar
	408. also created dummy data as 'context'
9. To create a super user for the Administrator page, run
```
ptyhon manage.py makemigrations
python manage.py runserver
python manage.py createsuperuser
```
	009. you can now login, in /admin page
	109. click users to see your users
	209. you can edit info, check current users/groups/etc. 
	309. django doesnt store your actual passwords, it automatically hashes them
10. Create models class in your models.py file in your app directory
	010. run python manage.py makemigrations
	110. this creates a 0001_intial.py file under migrations sub-directory
	210. to create this table in your database, run 
	```
	python manage.py sqlmigrate blog 0001
	python manage.py sqlmigrate <appName> <migrationNumber>
	``` 
	310. After you create model class and create your table, run the migrate command 
	```
	python manage.py migrate
	```
	410. Migrations are so useful bc they allow us to make changes to our databses even after its created and has existing data in the database
	510. if you wanted to query the database using these models, you can access the shell by running
	```
	python manage.py shell
	```
	610. example commands in the shell
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
	710. go to app->views.py and replace dummy data with our post model
		- from .models import Post 
		- context -> posts -> Post.objects.all() 
		- to see the Post datatable in your /admin page, register it to your admin.py file in your app directory
		- import it again, then do admin.site.register(Post)
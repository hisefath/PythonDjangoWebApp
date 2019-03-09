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







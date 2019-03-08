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
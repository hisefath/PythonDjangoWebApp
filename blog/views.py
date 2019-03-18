from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Sefath Chowdhury',
		'price': '$40',
        'title': 'Textbook title 1',
        'details': 'textbook post details',
        'date_posted': 'Feburary 27, 2018'
    },
     {
        'author': 'John Doe',
		'price': '$70',
        'title': 'Textbook title 2',
        'details': 'textbook post details',
        'date_posted': 'Feburary 28, 2018'
    }
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
	
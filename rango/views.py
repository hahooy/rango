from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {
		'boldmessage': 'I am bold font from the context',
		'rango_pic': "rango/images/rango-picture.png"
	}
	return render(request, 'rango/index.html', context)

def about(request):
	return HttpResponse('<p>Django says this is the about page</p><a href="/rango">to index page</a>')
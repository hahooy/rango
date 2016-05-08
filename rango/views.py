from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
	context = {
		'boldmessage': 'I am bold font from the context',
		'rango_pic': "rango/images/rango-picture.png",
		'categories_set': Category.objects.all()
	}
	return render(request, 'rango/index.html', context)

def about(request):
	return render(request, 'rango/about.html', {})

def category(request, category_name_slug):
	context = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		context['category_name'] = category.name

		pages = Page.objects.filter(category=category)

		context['pages'] = pages
		context['category'] = category

	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context)
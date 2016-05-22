from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm

def index(request):
	context = {
		'boldmessage': 'I am bold font from the context',
		'rango_pic': "rango/images/rango-picture.png",
		'categories_set': Category.objects.all(),
		'top_five_viewed_pages': Page.objects.all().order_by('-views')[:5]
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

def add_category(request):
	# HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage
			return index(request)
		else:
			# The suplied form contained errors
			print form.errors

	else:
		# if the request was not a POST, display the form to enter details
		form = CategoryForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request, 'rango/add_category.html', {'form': form})




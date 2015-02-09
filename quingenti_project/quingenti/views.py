from django.template import RequestContext
from django.shortcuts import render_to_response
from quingenti import models
from quingenti.forms import GigForm

def index(request):
    
	context = RequestContext(request)
	category_list = models.Category.objects.order_by('name')
	context_dict = {'categories': category_list}
	
	for category in category_list:
		category.url = category.name.replace(' ', '_')
    
	return render_to_response('quingenti/index.html', context_dict, context)
	
def category(request, category_name_url):
	
	context = RequestContext(request)
	
	category_name = category_name_url.replace('_', ' ')
	
	context_dict = {'category_name': category_name}
	
	try:
	
		category = models.Category.objects.get(name=category_name)
		
		gigs = models.Gig.objects.filter(category=category)
		
		context_dict['gigs'] = gigs
		
		context_dict['category'] = category
	except models.Category.DoesNotExist:
	
		pass
		
	gig_list = models.Gig.objects.filter(category=category).order_by('title')
	context_dict['gig_list'] = gig_list
	
	for gig in gig_list:
		#gig.url = gig.title.replace(' ', '_')
		gig.url = gig.id
		
	return render_to_response('quingenti/category.html', context_dict, context)
	
def gig(request, gig_id_url):
	
	context = RequestContext(request)
	
	gig_id = gig_id_url
	gig = models.Gig.objects.get(id=gig_id)
	gig_title = gig.title
	gig_description = gig.description
	gig_price = gig.price
	
	context_dict = {'gig_title': gig_title}
	context_dict['gig_id'] = gig_id
	context_dict['gig_description'] = gig_description
	context_dict['gig_price'] = gig_price
	
	try:	
		gig = models.Gig.objects.get(title=gig_title)
		context_dict['gig'] = gig
	except models.Gig.DoesNotExist:
	
		pass	
		
	return render_to_response('quingenti/gig.html', context_dict, context)
	


def add_category(request):
    # Get the context from the request.
	context = RequestContext(request)

    # A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
		if form.is_valid():
            # Save the new category to the database.
			form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
			return index(request)
		else:
            # The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
        # If the request was not a POST, display the form to enter details.
		form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
	return render_to_response('quingenti/add_category.html', {'form': form}, context)
	
def add_gig(request):
    # Get the context from the request.
	context = RequestContext(request)

    # A HTTP POST?
	if request.method == 'POST':
		form = GigForm(request.POST)

        # Have we been provided with a valid form?
		if form.is_valid():
            # Save the new category to the database.
			form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
			return index(request)
		else:
            # The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
        # If the request was not a POST, display the form to enter details.
		form = GigForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
	return render_to_response('quingenti/add_gig.html', {'form': form}, context)
	

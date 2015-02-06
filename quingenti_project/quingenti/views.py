from django.template import RequestContext
from django.shortcuts import render_to_response
from quingenti import models

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
		
	return render_to_response('quingenti/category.html', context_dict, context)

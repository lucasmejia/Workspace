from django.conf.urls import patterns, include, url
from quingenti import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', views.index, name='index'),
    # url(r'^quingenti_project/', include('quingenti_project.foo.urls')),

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^quingenti/add_category/$', views.add_category, name='add_category'),
	url(r'^quingenti/add_gig/$', views.add_gig, name='add_gig'),
	url(r'category/(?P<category_name_url>\w+)/$', views.category, name='category'),
	url(r'gig/(?P<gig_id_url>\w+)/$', views.gig, name='gig'),
)

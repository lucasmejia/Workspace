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
	url(r'category/(?P<category_name_url>\w+)/$', views.category, name='category'),
)

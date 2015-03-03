from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_bookmarks.bookmarks.views import *
from django.views.generic import *
import os.path

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', main_page),
	url(r'^user/(\w+)/$', user_page),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': site_media}),
	url(r'^register/$', register_page),
	url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html/')),
)


from django.conf.urls import patterns, url, include
from shifts_app.forms import RunForm


urlpatterns = patterns('shifts_app.views',
    url(r'^inline-formset/$', 'inline_formset',
       {'form_class': RunForm, 'template': 'example/inline-formset.html'}, name='create'),
    url(r'^(?P<id>\d+)/$', 'view_detail', name='detail'),
    url(r'^(?P<id>\d+)/delete/$', 'view_delete', name='delete'),
    url(r'^list/$', 'view_list', name='list'),
    url(r'^$', 'home', name='home'),
    url(r'^(?P<id>\d+)/update$', 'view_update', {'form_class': RunForm, 'template': 'example/update.html'}, name='update'),
    url(r'^create/$', 'post_creator', name='creator'),
    url(r'^post/$', 'post_create', name='post'),
    url(r'^connect/(?P<operation>.+)/(?P<id>\d+)/(?P<pk>\d+)/$', 'change_posts', name='change_posts'),
    url(r'^cover/$', 'post_view', name='cover'),
    url(r'^select/$', 'cover_post', name='coverer'),
    url(r'^what/(?P<id>\d+)/(?P<pk>\d+)/(?P<opk>\d+)/(?P<oid>\d+)/$', 'cover', name='covering')

    # url(r'^posts/$', 'post_view', name='posts'),
	# url(r'^(?P<id>\d+)/select/$', 'select', name='delete'),

)


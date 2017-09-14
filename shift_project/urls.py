import django
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'', include('shifts_app.urls', namespace='shift')),
    url(r'^admin/', admin.site.urls),
)


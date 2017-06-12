from django.conf.urls import url
from django.contrib import admin
from photos.views import hello
from photos.views import detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$',
    	detail, name='detail'),  
]
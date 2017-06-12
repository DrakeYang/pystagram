from django.conf.urls import url
from django.contrib import admin
from photos.views import hello,detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$',detail, name='detail'),
    url(r'^hidden-photos/(?P<pk>[0-9]+)$', detail, kwargs={'hidden':True}),
]
urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
from django.conf.urls import include, url
from django.conf.urls.static import static
from .secret_key import PROD
from . import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('stories.urls', namespace='stories')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    #url(r'^author/', include('stories.urls', namespace='suthors')),
]

#separate urls from developement server and production
if not PROD:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    url(r'^$', 'documentary.views.home', name='home'),
    url(r'^documentary/', include('documentary.urls', namespace="documentary")),
    # url(r'^$', 'hobby.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about$', 'documentary.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

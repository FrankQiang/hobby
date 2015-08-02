from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^title/add/$', views.title_add, name='title_add'),
    url(r'^title/show/$', views.title_show, name='title_show'),
    url(r'^title/batch/add/$', views.title_batch_add, name='title_batch_add'),
    url(r'^title/page/(\d+)$', views.title_page, name='title_page'),
    url(r'^site/add/$', views.site_add, name='site_add'),
    url(r'^site/show/(\d+)$', views.site_show, name='site_show'),
    url(r'^site/batch/add/$', views.site_batch_add, name='site_batch_add'),
    url(r'^error$', views.error, name='error'),
]
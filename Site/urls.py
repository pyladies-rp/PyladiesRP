
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^members/$', views.pyladies, name='pyladies_list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]

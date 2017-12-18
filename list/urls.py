from django.conf.urls import include, url

from list import views

urlpatterns = [

    url(r'^$', views.home),
    url(r'^create/$', views.create),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_check/$', views.add_check, name='add_check')

]
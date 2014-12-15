from django.conf.urls import patterns, url

from OGS import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'^search/$', views.search),
                       url(r'^second/$', views.index2),
                       url(r'^second/search/$', views.search2),
)
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start-a-space$', views.starting, name='starting'),
    url(r'^join$', views.join, name='join'),
    url(r'^join/supporter$', views.join_supporter, name='join_supporter'),
    url(r'^spaces$', views.spaces, name='spaces'),
    url(r'^space_detail$', views.space_detail, name='space_detail'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
]

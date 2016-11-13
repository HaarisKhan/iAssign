from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^home/$', views.Home, name='home'),
    url(r'^signup/$', views.SignUp, name='signup'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
    ]
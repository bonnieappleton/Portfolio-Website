from django.conf.urls import url

from . import views

# Prefixed with '/blog/'
urlpatterns = [
    url(r'^$', views.Blog.as_view(), name='blog'),
]
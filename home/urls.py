from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='home'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccess.as_view(), name='contact-success'),
    url(r'^js-projects/$', views.JSProjects.as_view(), name='js-projects'),
    url(r'^js-projects/books$', views.JSBooks.as_view(), name='js-books'),
]
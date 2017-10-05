from django.conf.urls import url

from . import views

# Prefixed with '/page-analyser/'
urlpatterns = [
    url(r'^$', views.PageAnalyser.as_view(), name='page-analyser'),
    url(r'^analyser-report/$', views.AnalyserReport.as_view(), name='analyser-report'),
]
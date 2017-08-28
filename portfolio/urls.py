from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'^googlea14532fb912s486\.html$', lambda r: HttpResponse("google-site-verification: google6430b1c1c5f4d50f.html", mimetype="text/plain")),
]

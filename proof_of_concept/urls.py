from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
 
#importing the views we created 
from . import views
from python import test
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    #defining a new URL pattern
    #when we will go here our template will render
    url(r'^$', views.index),

    url(r'^home', views.index, name="home"),

    url(r'^rungenerallikiehood/', views.runscript),

    url(r'^runtraitfrequencies/', views.runtraitfrequencies),

    url(r'^getdata/', views.getformdata),

    url(r'^example/', views.example),

    url(r'^showdata/', views.showdata),

    url(r'^test/', views.test),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
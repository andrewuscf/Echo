from django.conf.urls import patterns, include, url
from django.contrib import admin
from Main import views

urlpatterns = patterns('',
    url(r'^api/', include('Main.api.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home)
)

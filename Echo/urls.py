from django.conf.urls import *
from django.contrib import admin
from Main import views

urlpatterns = patterns('',
    url(r'^api/', include('Main.api.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Main.views.home', name='home'),
    url(r'^main/', 'Main.views.main', name='main'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'MainPage.html'}, name='login'),
)

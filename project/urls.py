from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app import views as app_views

urlpatterns = [
    url(r'^$', app_views.home, name='home'),
    url(r'^login/$', app_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
    url(r'^settings/$', app_views.settings, name='settings'),
    url(r'^settings/password/$', app_views.password, name='password'),
]

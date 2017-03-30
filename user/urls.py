from django.conf.urls import include, url
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^finduser', views.find_user),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

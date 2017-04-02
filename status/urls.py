from django.conf.urls import include, url
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^getstatus', views.get_new_status),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

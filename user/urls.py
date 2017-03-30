from django.conf.urls import include, url
from . import views
from rest_framework import routers, serializers, viewsets

#router = routers.DefaultRouter()
#router.register(r'login', , 'login')

urlpatterns = [
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

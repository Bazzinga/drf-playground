from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import url, patterns, include
from rest_framework import viewsets, routers
from apitest.models import MyModel
from apitest.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'mymodel', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
                            url(r'^', include(router.urls)),
                            url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                        )
# from django.contrib import admin
# admin.autodiscover()


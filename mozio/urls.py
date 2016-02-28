"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1/providers/$', views.ProviderList.as_view()),
    url(r'^api/v1/providers/(?P<pk>.*)/$', views.ProviderDetail.as_view()),
    url(r'^api/v1/service-area/$', views.ServiceAreaList.as_view()),
    url(r'^api/v1/service-area/(?P<pk>.*)/$', views.ServiceAreaDetail.as_view()),
    url(r'^api/v1/find-service-area', views.FindServiceArea.as_view()),
    url(r'^api/v1/get-multi-service-area/$', views.BatchGetServiceArea.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),

]

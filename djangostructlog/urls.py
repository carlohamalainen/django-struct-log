"""djangostructlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

from structlog.models import LogItem
admin.site.register(LogItem)

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class LogItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LogItem
        fields = ('name', 'host', 'user', 'description', 'attributes', 'created_at', 'updated_at',)

class LogItemViewSet(viewsets.ModelViewSet):
    queryset = LogItem.objects.all()
    serializer_class = LogItemSerializer

router = routers.DefaultRouter()
router.register(r'logitems', LogItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

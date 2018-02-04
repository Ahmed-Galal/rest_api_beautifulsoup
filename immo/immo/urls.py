"""immo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from reekomer.viewsets.edition import EditionViewSet
from reekomer.viewsets.habitation import HabitationViewSet
from reekomer.viewsets.immeuble import ImmeubleViewSet
from reekomer.viewsets.immo import ImmoViewSet
from reekomer.viewsets.region import RegionViewSet
from reekomer.viewsets.scarping import ScarpingView

router = DefaultRouter()
router.register(prefix='edition', viewset=EditionViewSet)
router.register(prefix='habitation', viewset=HabitationViewSet)
router.register(prefix='immeuble', viewset=ImmeubleViewSet)
router.register(prefix='immo', viewset=ImmoViewSet)
router.register(prefix='region', viewset=RegionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^scarp/$', ScarpingView),
]

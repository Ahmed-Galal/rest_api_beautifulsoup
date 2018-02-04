from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers.reekomer import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework


class Filter(rest_framework.FilterSet):
    class Meta:
        model = Region
        fields ='__all__'

class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = Filter
    search_fields = ['date', 'price','code_postal', 'price_msquare','place', 'typeImo',
                  'size', 'charac','description', 'link','website', 'image','idannonce','phone_number']
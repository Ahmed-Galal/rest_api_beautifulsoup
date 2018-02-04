from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers.reekomer import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework


class Filter(rest_framework.FilterSet):
    class Meta:
        model = Habitation
        fields = '__all__'

class HabitationViewSet(ModelViewSet):
    queryset = Habitation.objects.all()
    serializer_class = HabitationSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = Filter
    search_fields = ['date', 'price','code_postal', 'price_msquare','place', 'typeImo',
                  'size', 'charac','description', 'link','website', 'image','idannonce','phone_number']
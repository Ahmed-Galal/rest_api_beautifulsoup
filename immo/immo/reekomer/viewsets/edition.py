from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers.reekomer import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework


class Filter(rest_framework.FilterSet):
    class Meta:
        model = Edition
        fields =['type_immo', 'numero','rue', 'intitule','ville', 'code_postal',
                  'adresse', 'surface','sous_sol', 'etages','fai', 'prix','commission'
        ,'loyer' ,'loue' ,'eof_bail' ,'date_entre' ,'description' ,'prix_m2' ,'rentabilite'
        ,'remb_moyen' ,'interet','ecart' ,'agence','name' ,'telephone','mail' ,'link'
        ,'montant' ,'label','archive' ,'vendu','achete' ,'offre','date_offre']

class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = Filter
    search_fields = ['type_immo', 'numero','rue', 'intitule','ville', 'code_postal',
                  'adresse', 'surface','sous_sol', 'etages','fai', 'prix','commission'
        ,'loyer' ,'loue' ,'eof_bail' ,'date_entre' ,'description' ,'prix_m2' ,'rentabilite'
        ,'remb_moyen' ,'interet','ecart' ,'agence','name' ,'telephone','mail' ,'link'
        ,'montant' ,'label','archive' ,'vendu','achete' ,'offre','date_offre']
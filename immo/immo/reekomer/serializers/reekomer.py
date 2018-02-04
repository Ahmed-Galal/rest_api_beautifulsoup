from rest_framework import serializers

from ..models import Habitation
from ..models import Edition
from ..models import Immeuble
from ..models import Immo
from ..models import Region


class HabitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitation
        fields = '__all__'

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'

class ImmeubleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immeuble
        fields = '__all__'

class ImmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immo
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

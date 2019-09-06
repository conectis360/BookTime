from rest_framework import serializers, viewsets
from . import models

class OrderLineSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.StringRelatedField()
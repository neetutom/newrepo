from rest_framework import serializers
from .models import apimodels

class apiserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apimodels
        fields = ('title', 'description')
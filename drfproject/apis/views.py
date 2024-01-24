from django.shortcuts import render
from rest_framework import viewsets
from .models import apimodels
from .serializers import apiserializers

# Create your views here.
class apiViewSet(viewsets.ModelViewSet):
    queryset = apimodels.objects.all()

    serializer_class = apiserializers
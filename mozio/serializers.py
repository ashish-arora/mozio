__author__ = 'ashish'

from django.forms import widgets
from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from mozio.models import Providers, ServiceArea

class ProvidersSerializer(DocumentSerializer):

    class Meta:
        model = Providers
        fields = ('id', 'name', 'email', 'phone_number', 'language', 'currency')


class ServiceAreaSerializer(DocumentSerializer):
    #provider = StringField()

    class Meta:
        model = ServiceArea
        fields = ('id', 'provider', 'loc', 'name', 'price')

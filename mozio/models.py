__author__ = 'ashish'

from mongoengine import *

LANGUAGE_CHOICES = ('English', 'Spanish', 'French', 'Hindi', 'Japneese')

CURRENCY_CHOICES = ('USD', 'SGD', 'AUD', 'INR')


class Providers(Document):
    name = StringField(max_length=20, required=True)
    email = EmailField(required=True)
    phone_number = StringField(required=True, max_length=11)
    language = StringField(required=True, choices=LANGUAGE_CHOICES)
    currency= StringField(required=True, choices=CURRENCY_CHOICES)

class ServiceArea(Document):
    provider = ReferenceField(Providers)
    loc = PolygonField()
    name = StringField(required=True)
    price = FloatField(required=True)


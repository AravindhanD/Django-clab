from rest_framework import serializers
from .models import *
class clabserializer(serializers.ModelSerializer):
     

     class Meta:
          model = Account
          fields =('__all__')
     
class destiserializer(serializers.ModelSerializer):
     

     class Meta:
          model = Destination
          fields =('__all__')
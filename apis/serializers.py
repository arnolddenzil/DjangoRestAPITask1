# import serializer from rest_framework
from rest_framework import serializers
from django.contrib.auth.models import User

# import model from models.py
from .models import SimpleUser


# Create a model serializer
class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ('username', 'password')

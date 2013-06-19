from rest_framework import serializers
from apitest.models import MyModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyModel
        fields = ('x', 'y')

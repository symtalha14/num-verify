from rest_framework import serializers
from sample.models import Demo

class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demo
        fields='__all__'
        
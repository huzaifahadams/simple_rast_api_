from attr import field
from rest_framework import serializers

from drfapp.models import stuff

class stuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = stuff
        fields = '__all__'
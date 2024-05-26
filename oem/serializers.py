from rest_framework import serializers
from oem.models import OemDetail


class OemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OemDetail
        fields = ["id", "manufacturer", "oemModel", "yearModel", "origin"]

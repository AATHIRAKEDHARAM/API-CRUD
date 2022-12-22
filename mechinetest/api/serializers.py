from rest_framework import serializers
from.models import *


class CreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["ItemName", "MRP"]


class UpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["ItemName", "MRP"]

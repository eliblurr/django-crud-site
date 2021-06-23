from rest_framework import serializers
from .models import Item, Message


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Message
        fields = '__all__'
from rest_framework import serializers
from .models import Stack


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": True
            },
        }

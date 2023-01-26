from rest_framework import serializers
from .models import Application
from stacks.models import Stack
from status.models import Status, StatusOptions

from status.serializers import StatusSerializer
from stacks.serializers import StackSerializer
import ipdb


class ApplicationSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many=True)
    status = StatusSerializer(many=True)

    class Meta:
        model = Application
        fields = ['id', 'title', 'company', 'link', 'obs',
                  'level', 'develop', 'stacks', 'status']

    def create(self, validated_data):
        stacks_data = validated_data.pop('stacks')
        status_data = validated_data.pop('status')

        user = self.context['request'].user

        application = Application.objects.create(user=user, **validated_data)

        for stack in stacks_data:
            stack_inst, _ = Stack.objects.get_or_create(**stack)
            application.stacks.add(stack_inst)

        for status in status_data:
            status_inst, _ = Status.objects.get_or_create(**status)
            application.status.add(status_inst)
        return application


class ApplicationDetailsSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True, read_only=True)
    stacks = StackSerializer(many=True, read_only=True)

    class Meta:
        model = Application

        fields = ["id",
                  "title",
                  "company",
                  "link",
                  "obs",
                  "level",
                  "develop",
                  "stacks",
                  "status",
                  ]

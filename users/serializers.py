
from rest_framework import serializers
from .models import User
from applications.serializers import ApplicationSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = "__all__"
        read_only_fields = ['id', "applications"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_applications(self, obj):
        applications = obj.applications.all()
        serializer = ApplicationSerializer(applications, many=True)
        return serializer.data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    applications = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = ["id", "last_login", "username", "first_name",
                  "last_name",  "email", "applications"]
        read_only_fields = ['id', "applications"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_applications(self, obj):
        applications = obj.applications.all()
        serializer = ApplicationSerializer(applications, many=True)
        return serializer.data


class UserDetailsSerializer(serializers.ModelSerializer):
    applications = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'applications']

    def get_applications(self, obj):
        applications = obj.applications.all()
        serializer = ApplicationSerializer(applications, many=True)
        return serializer.data

from django.shortcuts import render
from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer, ApplicationDetailsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from status.models import Status
from stacks.models import Stack
from rest_framework.response import Response
from users.permissions import IsOwner

import ipdb

# Create your views here.


class ApplicationCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationDetailsSerializer

    lookup_field = "id"


class StatusUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationDetailsSerializer

    lookup_field = "id"

    def update_status(self, request, *args, **kwargs):
        instance = self.get_object()
        status_data = request.data.get('status_name')
        if status_data:
            status, _ = Status.objects.get_or_create(status=status_data)
            instance.status.clear()
            instance.status.add(status)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"error": "status_name is required."}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.update_status(request, *args, **kwargs)


class StacksUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationDetailsSerializer

    lookup_field = "id"

    def update_stacks(self, request, *args, **kwargs):
        instance = self.get_object()
        stacks_data = request.data.get('stacks_name')

        if stacks_data:
            instance.stacks.clear()
            for stack in stacks_data:
                stack, _ = Stack.objects.get_or_create(stack=stack)
                instance.stacks.add(stack)

            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"error": "stacks_name is required."}, stack=stack.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.update_stacks(request, *args, **kwargs)

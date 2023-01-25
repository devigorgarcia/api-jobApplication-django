from django.shortcuts import render
from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ApplicationCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

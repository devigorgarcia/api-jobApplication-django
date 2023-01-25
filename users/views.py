from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserDetailsSerializer
from .permissions import IsOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    lookup_field = "id"

import ipdb
from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserDetailsSerializer, UserProfileSerializer
from .permissions import IsOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ListUserProfileView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    lookup_field = "id"

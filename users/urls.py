from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('users/', CreateUserView.as_view()),
    path('users/<str:id>/', UserDetailsView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]

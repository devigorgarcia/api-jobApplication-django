from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('user/', CreateUserView.as_view()),
    path('user/profile/', ListUserProfileView.as_view()),
    path('user/<str:id>/', UserDetailsView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]

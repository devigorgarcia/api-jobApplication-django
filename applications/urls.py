from django.urls import path
from .views import *

urlpatterns = [
    path('applications/', ApplicationCreateView.as_view())
]

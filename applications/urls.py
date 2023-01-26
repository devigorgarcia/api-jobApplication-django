from django.urls import path
from .views import *

urlpatterns = [
    path('applications/', ApplicationCreateView.as_view()),
    path('applications/<str:id>/', ApplicationDetailView.as_view()),
    path('applications/status/<str:id>/', StatusUpdateView.as_view()),
    path('applications/stacks/<str:id>/', StacksUpdateView.as_view())
]

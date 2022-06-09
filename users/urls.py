from django.urls import path
from .views import UserRegisterView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    # path('profile/<int:pk>', UserSettings.as_view(), name='profile'),
]

from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('user/register', views.register, name='register'),
]
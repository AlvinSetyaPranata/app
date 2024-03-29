
from django.contrib import admin
from django.urls import path
from .views import Registrasi

urlpatterns = [
    path('', Registrasi.as_view(), name="registrasi"),
]

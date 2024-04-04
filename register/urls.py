
from django.contrib import admin
from django.urls import path
from .views import (
    FormRegistrasi,
    SiswaList,
    OrangTuaList
)

urlpatterns = [
    path('', FormRegistrasi.as_view(), name="registrasi"),
    path('api/siswa', SiswaList.as_view(), name="daftar-siswa"),
    path('api/orangtua', OrangTuaList.as_view(), name="daftar-siswa"),
]

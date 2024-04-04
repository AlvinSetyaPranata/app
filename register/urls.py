
from django.contrib import admin
from django.urls import path, re_path
from .views import (
    FormRegistrasi,
    SiswaList,
    OrangTuaList,
    SiswaDetails,
    OrangTuaDetails
)

urlpatterns = [
    path('', FormRegistrasi.as_view(), name="registrasi"),
    path('api/siswa', SiswaList.as_view(), name="daftar-siswa"),
    path('api/orangtua', OrangTuaList.as_view(), name="daftar-orangtua"),
    path('api/siswa/<int:pk>', SiswaDetails.as_view(), name="data-siswa"),
    path('api/orangtua/<int:pk>', OrangTuaDetails.as_view(), name="data-orangtua"),
]

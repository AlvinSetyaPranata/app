from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from json import loads
from .models import (
    Siswa,
    OrangTua
)

class Registrasi(View):
    def get(self, request):
        return render(request, "index.html")


    def post(self, request):

        data = request.POST

        model_ibu = OrangTua.objects

        # Konversi json string ke json object
        data_ayah = loads(data["ayah"])
        data_ibu = loads(data["ibu"])


        model_ayah = OrangTua.objects.create(**data_ayah)
        model_ibu = OrangTua.objects.create(**data_ibu)

        model_ayah.save()
        model_ibu.save()


        model_siswa = Siswa.objects.create(ayah=model_ayah, ibu=model_ibu, **data["siswa"])
        model_siswa.save()

        return HttpResponse("<h1>Succes<<h2>")


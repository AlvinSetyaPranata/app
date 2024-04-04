from json import loads
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import (
    SiswaSerializer,
    OrangTuaSerializer
)

from .models import (
    Siswa,
    OrangTua
)

class FormRegistrasi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, "index.html")


    def post(self, request):

        data = request.POST

        model_ibu = OrangTua.objects

        # Konversi json string ke json object
        data_ayah = loads(data["ayah"])
        data_ibu = loads(data["ibu"])
        data_siswa = loads(data["siswa"])

        print(data_ayah)


        model_ayah = OrangTua.objects.create(**data_ayah)
        model_ibu = OrangTua.objects.create(**data_ibu)
        model_siswa = Siswa.objects.create(ayah=model_ayah, ibu=model_ibu, **data_siswa)

        model_ayah.save()
        model_ibu.save()
        model_siswa.save()

        return HttpResponse("<h1>Succes<<h2>")


class SiswaList(APIView):
    permission_classes = [AllowAny]
    
    def get(self, _):
        data = SiswaSerializer(Siswa.objects.all(), many=True)

        return Response(data.data)
    

class OrangTuaList(APIView):
    permission_classes = [AllowAny]

    def get(self, _):
        data = OrangTuaSerializer(OrangTua.objects.all(), many=True)

        return Response(data.data)
    

class SiswaDetails(APIView):
    permission_classes = [AllowAny]

    def get(self, _, pk):

        query_data = Siswa.objects.filter(pk=pk)

        if not query_data:
            return Response({"Messege" : f"Tidak ada data dengan id {pk}"}, status=status.HTTP_404_NOT_FOUND)

        data = SiswaSerializer(query_data[0], many=True)

        return Response(data.data)

class OrangTuaDetails(APIView):
    permission_classes = [AllowAny]

    def get(self, _, pk):

        query_data = OrangTua.objects.filter(pk=pk)

        if not query_data:
            return Response({"Messege" : f"Tidak ada data dengan id {pk}"}, status=status.HTTP_404_NOT_FOUND)

        data = OrangTuaSerializer(query_data[0])

        return Response(data.data)
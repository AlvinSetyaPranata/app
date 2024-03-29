from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse


class Registrasi(View):
    def get(self, request):
        return render(request, "index.html")


    def post(self, request):
        print(request.POST)
        return HttpResponse("<h1>Succes<<h2>")


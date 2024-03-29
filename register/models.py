from django.db import models

# Create your models here.

class OrangTua:
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateTimeField()
    jenis_kelamin = models.CharField(max_length=1)
    asal_sekolah = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)



class Siswa:
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateTimeField()
    jenis_kelamin = models.CharField(max_length=1)
    asal_sekolah = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)
    ayah = models.ForeignKey(OrangTua, on_delete=models.CASCADE)
    ibu = models.ForeignKey(OrangTua, on_delete=models.CASCADE)





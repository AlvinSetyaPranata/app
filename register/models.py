from django.db import models

# Create your models here.

class OrangTua(models.Model):
    nik = models.IntegerField()
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=1)
    asal_sekolah = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255, null=True, blank=True)


class Siswa(models.Model):
    nik = models.IntegerField()
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=1)
    alamat = models.CharField(max_length=255)
    ayah = models.ForeignKey(OrangTua, on_delete=models.CASCADE, related_name="ayah")
    ibu = models.ForeignKey(OrangTua, on_delete=models.CASCADE, related_name="ibu")

from django.test import TestCase
from .models import (
    Siswa,
    OrangTua
)

# Create your tests here.
class SiswaTestCase(TestCase):
    def setUp(self):

        self.ayah = OrangTua.objects.create(
            nik=3528042402053401,
            nama="Howard Stark",
            tanggal_lahir="1978-01-13",
            jenis_kelamin="L",
            asal_sekolah="SMK Negeri 1 Pamekasan",
            alamat="Jl. Dirgahayu no 55, Pamekasan",
            pekerjan="Pegawai Swasta"
        )

        self.ibu = OrangTua.objects.create(
            nik=3528042502050002,
            nama="Stephanie Mcmachon",
            tanggal_lahir="1980-01-13",
            jenis_kelamin="P",
            asal_sekolah="SMK Negeri 3 Pamekasan",
            alamat="Jl. Dirgahayu no 55, Pamekasan",
            pekerjan="Ibu Rumah Tangga"
        )

        self.siswa = Siswa.objects.create(
            nik=3528042452050003,
            nama="Tony Stark",
            tanggal_lahir="2005-02-24",
            jenis_kelamin="L",
            asal_sekolah="SMK Negeri 1 Pamekasan",
            alamat="Jl. Dirgahayu no 55, Pamekasan",
            ayah=self.ayah,
            ibu=self.ibu
        )
class OrangTuaTestCase(TestCase):
    def setUp(self):

        self.ayah = OrangTua.objects.create(
            nik=3528042402053401,
            nama="Howard Stark",
            tanggal_lahir="1978-01-13",
            jenis_kelamin="L",
            asal_sekolah="SMK Negeri 1 Pamekasan",
            alamat="Jl. Dirgahayu no 55, Pamekasan",
            pekerjan="Pegawai Swasta"
        )

        self.ibu = OrangTua.objects.create(
            nik=3528042502050002,
            nama="Stephanie Mcmachon",
            tanggal_lahir="1980-01-13",
            jenis_kelamin="P",
            asal_sekolah="SMK Negeri 3 Pamekasan",
            alamat="Jl. Dirgahayu no 55, Pamekasan",
            pekerjan="Ibu Rumah Tangga"
        )

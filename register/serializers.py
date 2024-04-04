from rest_framework.serializers import ModelSerializer
from .models import (
    OrangTua,
    Siswa
)



class OrangTuaSerializer(ModelSerializer):
    class Meta:
        model = OrangTua
        fields = '__all__'


class SiswaSerializer(ModelSerializer):
    ayah = OrangTuaSerializer()
    ibu = OrangTuaSerializer()

    class Meta:
        model = Siswa
        fields = '__all__'


# Generated by Django 5.0.4 on 2024-04-04 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_orangtua_jenis_kelamin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siswa',
            name='asal_sekolah',
        ),
    ]

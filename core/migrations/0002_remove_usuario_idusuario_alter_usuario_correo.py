# Generated by Django 4.0.4 on 2022-06-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idUsuario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Correo usuario'),
        ),
    ]

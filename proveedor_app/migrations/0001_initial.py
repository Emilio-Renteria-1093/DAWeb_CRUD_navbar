# Generated by Django 5.1 on 2024-12-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('Id_Proveedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=300)),
                ('Ruta', models.CharField(max_length=300)),
                ('Sucursales', models.CharField(max_length=3)),
                ('Num_Tel', models.CharField(max_length=10)),
                ('Metodo_Trans', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-11-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('Id_Servicio', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Tipo_Servicio', models.CharField(max_length=20)),
                ('Costo', models.CharField(max_length=20)),
                ('Material', models.CharField(max_length=20)),
                ('Fecha_inicio', models.DateTimeField()),
                ('Fecha_finalizado', models.DateTimeField()),
                ('Resolucion_Problema', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-12-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('Id_Nomina', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Id_Empleado', models.CharField(max_length=6)),
                ('Fecha_Pago', models.DateField()),
                ('Periodo_Pago', models.CharField(max_length=80)),
                ('Descripcion', models.CharField(max_length=300)),
                ('Total', models.CharField(max_length=1000)),
            ],
        ),
    ]
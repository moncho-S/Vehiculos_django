# Generated by Django 4.0.5 on 2023-07-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('fiat', 'Fiat'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('toyota', 'Toyota')], default='ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('particular', 'Particular'), ('transporte', 'Transporte'), ('carga', 'Carga')], default='particular', max_length=20)),
                ('motor', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

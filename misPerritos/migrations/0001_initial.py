# Generated by Django 2.0.9 on 2018-11-15 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='Fotos')),
                ('raza', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='misPerritos.Estado')),
            ],
        ),
    ]

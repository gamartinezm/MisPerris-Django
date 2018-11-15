# Generated by Django 2.0.9 on 2018-11-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
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
            name='Perro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('raza', models.CharField(default='Quiltro', max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]

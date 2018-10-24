# Generated by Django 2.0.9 on 2018-10-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RescatadosPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(upload_to='Foto')),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('estado', models.IntegerField(choices=[(1, 'Rescatado'), (2, 'Dsiponible'), (3, 'Adoptado'), (4, 'Seleccionar')], default=4)),
            ],
        ),
    ]

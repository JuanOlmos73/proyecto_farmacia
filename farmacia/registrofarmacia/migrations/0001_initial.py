# Generated by Django 3.2.4 on 2021-07-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20, verbose_name='clave del producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre del producto')),
                ('cantidad', models.IntegerField(verbose_name='cantidad del producto')),
                ('fecha_de_caducidad', models.DateField(verbose_name='fecha de caducidad')),
                ('descripcion', models.TextField(verbose_name='descripcion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'medicamento',
                'verbose_name_plural': 'medicamentos',
                'ordering': ['created'],
            },
        ),
    ]

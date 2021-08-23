# Generated by Django 3.2.4 on 2021-08-22 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrofarmacia', '0005_medicamentos_disponibilidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='salida_medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.TextField(default='', verbose_name='Nombre del paciente')),
                ('cantidad_suministrada', models.IntegerField(verbose_name='cantidad de medicamento suministrado')),
                ('fecha_suministrada', models.DateField(verbose_name='fecha suministrada')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrofarmacia.medicamentos', verbose_name='Medicamento')),
            ],
            options={
                'verbose_name': 'salidamedicamento',
                'verbose_name_plural': 'salidamedicamentos',
                'ordering': ['created'],
            },
        ),
    ]
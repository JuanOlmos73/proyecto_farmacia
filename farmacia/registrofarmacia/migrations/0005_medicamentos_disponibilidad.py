# Generated by Django 3.2.4 on 2021-08-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrofarmacia', '0004_auto_20210814_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamentos',
            name='disponibilidad',
            field=models.TextField(default='', verbose_name='disponibilidad'),
        ),
    ]

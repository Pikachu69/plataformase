# Generated by Django 2.2.1 on 2020-05-08 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SETyRS', '0011_auto_20200508_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial_admins_sinodal',
            old_name='departamento_id',
            new_name='nivel_educativo',
        ),
    ]
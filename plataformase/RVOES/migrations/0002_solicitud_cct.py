# Generated by Django 2.2.1 on 2020-05-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RVOES', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='cct',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.2.1 on 2019-09-11 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SigApp', '0012_auto_20190827_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasCuartoGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasPrimerGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasQuintoGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasSegundoGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasSextoGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosestadisticos',
            name='AlumnosIndigenasTercerGrado',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
    ]
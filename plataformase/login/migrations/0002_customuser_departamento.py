# Generated by Django 2.2.1 on 2020-04-07 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RVOES', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RVOES.Departamento'),
        ),
    ]

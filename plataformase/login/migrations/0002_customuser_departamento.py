# Generated by Django 3.0.3 on 2020-03-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Departamento'),
        ),
    ]

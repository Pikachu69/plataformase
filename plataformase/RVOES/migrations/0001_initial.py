# Generated by Django 2.2.1 on 2020-05-21 19:54

import RVOES.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Acuerdos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
                ('archivo', models.FileField(upload_to='Archivos/Acuerdos')),
                ('nivel', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_bibliograficos', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
                ('rec_didacticos', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
                ('talleres', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
                ('apoyo_informatico', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
                ('apoyo_comunicaciones', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
                ('personal', models.FileField(upload_to='Archivos/Academica', validators=[RVOES.validators.valid_extension])),
            ],
        ),
        migrations.CreateModel(
            name='CCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudio', models.FileField(upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('plan', models.FileField(upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('mapa', models.FileField(upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('programa', models.FileField(upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('metodologia', models.FileField(blank=True, null=True, upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('cifrhs', models.FileField(blank=True, null=True, upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('carta', models.FileField(blank=True, null=True, upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
            ],
        ),
        migrations.CreateModel(
            name='CInstitucional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitud', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('folio_pago', models.TextField(default='0', unique=True)),
                ('monto_pago', models.TextField(blank=True, null=True)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('pago', models.FileField(blank=True, null=True, upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('acredita_personalidad', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('acredita_inmueble', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('dictamen_suelo', models.TextField()),
                ('expediente_suelo', models.TextField(blank=True, null=True)),
                ('firma_suelo', models.TextField(blank=True, null=True)),
                ('fecha_suelo', models.DateField(blank=True, null=True)),
                ('licencia_suelo', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('dictamen_estructural', models.TextField()),
                ('fecha_estructural', models.DateField(blank=True, null=True)),
                ('arqui_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('DRO_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('noCedula_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('constancia_estructural', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('dictamen_proteccion', models.TextField(blank=True, null=True)),
                ('fecha_dictamen_proteccion', models.DateField(blank=True, null=True)),
                ('firma_dictamen_proteccion', models.TextField(blank=True, null=True)),
                ('constancia_proteccion', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('folio_inife', models.TextField()),
                ('fecha_inife', models.DateField(blank=True, null=True)),
                ('firma_inife', models.TextField(blank=True, null=True)),
                ('inife', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('des_instalacion', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('planos', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
                ('biblio', models.FileField(upload_to='Archivos/Institucional', validators=[RVOES.validators.valid_extension])),
            ],
        ),
        migrations.CreateModel(
            name='CMedSuperior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.FileField(blank=True, null=True, upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('folio_pago', models.TextField(default='0', unique=True)),
                ('monto_pago', models.TextField(blank=True, null=True)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('solicitud', models.FileField(upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('identificacion', models.FileField(upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('perDocente', models.FileField(upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('instalaciones', models.FileField(upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('dictamen_suelo', models.TextField(blank=True, null=True)),
                ('expediente_suelo', models.TextField(blank=True, null=True)),
                ('firma_suelo', models.TextField(blank=True, null=True)),
                ('fecha_suelo', models.DateField(blank=True, null=True)),
                ('dictamen_estructural', models.TextField(blank=True, null=True)),
                ('fecha_estructural', models.DateField(blank=True, null=True)),
                ('arqui_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('DRO_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('noCedula_dictamen_estructural', models.TextField(blank=True, null=True)),
                ('dictamen_proteccion', models.TextField(blank=True, null=True)),
                ('fecha_dictamen_proteccion', models.DateField(blank=True, null=True)),
                ('firma_dictamen_proteccion', models.TextField(blank=True, null=True)),
                ('folio_inife', models.TextField(blank=True, null=True)),
                ('fecha_inife', models.DateField(blank=True, null=True)),
                ('firma_inife', models.TextField(blank=True, null=True)),
                ('equipamiento', models.FileField(blank=True, null=True, upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('progEstuio', models.FileField(blank=True, null=True, upload_to='Archivos/MedSuperior', validators=[RVOES.validators.valid_extension])),
                ('cifrhs', models.FileField(blank=True, null=True, upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
                ('carta', models.FileField(blank=True, null=True, upload_to='Archivos/Curricular', validators=[RVOES.validators.valid_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateField(auto_now_add=True)),
                ('mostrado', models.CharField(blank=True, max_length=1, null=True)),
                ('archivo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('leida', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaNotificacion', models.DateField(auto_now_add=True)),
                ('tipo_notificacion', models.CharField(default='C', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='NotificacionRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, null=True)),
                ('nombres', models.TextField(blank=True, null=True)),
                ('curp', models.TextField(blank=True, null=True)),
                ('celular', models.TextField(blank=True, null=True)),
                ('leida', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaNotificacion', models.DateField(auto_now_add=True)),
                ('tipo_notificacion', models.CharField(default='C', max_length=2)),
                ('tipo_usuario', models.CharField(default='4', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField()),
                ('comentario', models.CharField(default='0', max_length=1)),
                ('nivel', models.CharField(max_length=1)),
                ('modalidad', models.CharField(max_length=1)),
                ('opcion', models.CharField(max_length=1)),
                ('salud', models.CharField(max_length=1)),
                ('completado', models.IntegerField(default='1')),
                ('noInstrumentoNotarial', models.IntegerField(blank=True, null=True)),
                ('nombreNotario', models.TextField(blank=True, null=True)),
                ('noNotario', models.IntegerField(blank=True, null=True)),
                ('nombreRepresentante', models.TextField(blank=True, null=True)),
                ('nombreSolicitud', models.TextField(blank=True, null=True)),
                ('cct', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

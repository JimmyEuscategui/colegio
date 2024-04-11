# Generated by Django 5.0.3 on 2024-04-10 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('idCurso', models.AutoField(primary_key=True, serialize=False)),
                ('curso', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('idSede', models.AutoField(primary_key=True, serialize=False)),
                ('sede', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('idEstudiante', models.AutoField(primary_key=True, serialize=False)),
                ('primerNombre', models.CharField(max_length=20)),
                ('segundoNombre', models.CharField(blank=True, max_length=20, null=True)),
                ('primerApellido', models.CharField(max_length=20)),
                ('segundoApellido', models.CharField(max_length=20)),
                ('documento', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(max_length=10)),
                ('foto', models.ImageField(upload_to='secretariaEstudiante')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('idCurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariaEstudiante.curso')),
                ('idTipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariaEstudiante.document')),
                ('idSede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariaEstudiante.sede')),
            ],
        ),
    ]

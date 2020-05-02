# Generated by Django 3.0.2 on 2020-05-01 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registroEquinos', '0003_auto_20200501_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_comp', models.CharField(max_length=255)),
                ('des_comp', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina_Deportiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=255)),
                ('descripcion_dis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prueba_campo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_raza', models.CharField(max_length=255)),
                ('des_raza', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_veterinario', models.CharField(max_length=255)),
                ('apellidos_veterinario', models.CharField(max_length=255)),
                ('correo_veterinario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_apertura', models.DateField()),
                ('estado', models.CharField(max_length=255)),
                ('observaciones', models.CharField(max_length=255)),
                ('veterinario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registroEquinos.Veterinario')),
            ],
        ),
        migrations.CreateModel(
            name='Equino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_equino', models.CharField(max_length=255)),
                ('fec_nacimiento', models.DateField()),
                ('adv_manejo', models.CharField(max_length=255)),
                ('sexo', models.BooleanField()),
                ('color', models.CharField(max_length=255)),
                ('comp_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registroEquinos.Comportamiento')),
                ('raza_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registroEquinos.Raza')),
            ],
        ),
    ]

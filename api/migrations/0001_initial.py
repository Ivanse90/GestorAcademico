# Generated by Django 4.0 on 2022-09-18 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('Nom_Asig', models.CharField(max_length=200)),
                ('cod_Asig', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('cod_asociado', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id_carrera', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_c', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('cod_e', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_e', models.CharField(max_length=200)),
                ('fech_ingreso', models.DateField()),
                ('tel_e', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('fech_nac', models.DateField()),
                ('carreras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='api.carreras')),
            ],
        ),
        migrations.CreateModel(
            name='Imparte',
            fields=[
                ('cod_imparte', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('grupo', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=200)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imparteAList', to='api.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('Nombre', models.CharField(max_length=200)),
                ('profesion', models.CharField(max_length=200)),
                ('codProfesor', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('cod_salon', models.IntegerField(primary_key=True, serialize=False)),
                ('edificio', models.CharField(max_length=200)),
                ('imparte', models.ManyToManyField(through='api.Asociado', to='api.Imparte')),
            ],
        ),
        migrations.CreateModel(
            name='Inscribe',
            fields=[
                ('cod_insc', models.IntegerField(primary_key=True, serialize=False)),
                ('semestre', models.IntegerField()),
                ('nota1', models.IntegerField()),
                ('nota2', models.IntegerField()),
                ('nota3', models.IntegerField()),
                ('definitiva', models.IntegerField()),
                ('estudiante', models.ManyToManyField(to='api.Estudiantes')),
                ('imparte', models.ManyToManyField(to='api.Imparte')),
            ],
        ),
        migrations.AddField(
            model_name='imparte',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ImpartePlist', to='api.profesor'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='imparte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asociadoIList', to='api.imparte'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asociadoSlist', to='api.salon'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ManyToManyField(through='api.Imparte', to='api.Profesor'),
        ),
    ]

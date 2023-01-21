from pyexpat import model
from django.db import models


class Profesor(models.Model):
    Nombre = models.CharField(max_length=200)
    profesion = models.CharField(max_length=200)
    codProfesor = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Nombre

class Asignatura(models.Model):
    Nom_Asig = models.CharField(max_length=200)
    cod_Asig = models.IntegerField(primary_key=True)
    profesor = models.ManyToManyField(Profesor, through='Imparte')
    def __str__(self):
        return self.Nom_Asig

class Imparte(models.Model):
    cod_imparte  = models.CharField(max_length=10, primary_key=True)
    grupo = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="ImpartePlist")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="imparteAList")
    def __str__(self):
        return str(self.cod_imparte + "-" + self.grupo)


class Carreras(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    nom_c = models.CharField(max_length=200)
    def __str__(self):
        return self.nom_c

class Estudiantes(models.Model):
    cod_e = models.IntegerField(primary_key=True)
    nom_e = models.CharField(max_length=200)
    fech_ingreso = models.DateField()
    tel_e = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fech_nac = models.DateField()
    carreras = models.ForeignKey(Carreras,on_delete=models.CASCADE, related_name="estudiantes")
    def __str__(self):
        return self.nom_e


class Inscribe(models.Model):
    cod_insc = models.IntegerField(primary_key=True)
    semestre = models.IntegerField()
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    nota3 = models.IntegerField()
    definitiva = models.IntegerField()
    imparte = models.ManyToManyField(Imparte)
    estudiante = models.ManyToManyField(Estudiantes)
    def __str__(self):
        return "Inscribe" + "-" + str(self.cod_insc)

class Salon(models.Model):
    cod_salon = models.IntegerField(primary_key=True)
    edificio = models.CharField(max_length=200)
    imparte = models.ManyToManyField(Imparte, through='Asociado')
    def __str__(self):
        return str(self.cod_salon)

class Asociado(models.Model):
    cod_asociado = models.CharField(max_length=10, primary_key=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="asociadoSlist")
    imparte = models.ForeignKey(Imparte, on_delete=models.CASCADE, related_name="asociadoIList")
    def __str__(self):
        return str(self.cod_asociado)










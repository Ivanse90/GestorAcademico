from rest_framework import serializers
from .models import Asignatura, Estudiantes, Profesor,Carreras,Imparte,Salon,Inscribe,Asociado





class EstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estudiantes
        fields = ['cod_e','nom_e','fech_ingreso','tel_e','direccion','fech_nac','carreras']
        depth = 1

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = "__all__"



class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['codProfesor','Nombre','profesion']

class AsignaturaSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(many=True,read_only=True)
    class Meta:
        model = Asignatura
        fields = ['cod_Asig','profesor','Nom_Asig']

class ImparteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imparte
        fields = "__all__"
        depth = 1

class ImparteSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Imparte
        fields = "__all__"

class InscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscribe
        fields = ['cod_insc','semestre','nota1','nota2','nota3','definitiva','imparte','estudiante']
        depth = 1

class InscribeSerializerIn(serializers.ModelSerializer):        
    class Meta:
        model = Inscribe
        fields = ['cod_insc','semestre','nota1','nota2','nota3','definitiva','imparte','estudiante']
        #depth = 1

    


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = "__all__"

class AsociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociado
        fields = "__all__"
        depth = 1

class AsociadoSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Asociado
        fields = "__all__"







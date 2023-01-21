from email.policy import HTTP
from .models import Asignatura, Asociado, Estudiantes, Carreras,Imparte, Inscribe, Profesor, Salon
from .serializers import AsociadoSerializer, AsociadoSerializerIn, EstudianteSerializer,CarreraSerializer, ImparteSerializerIn, InscribeSerializer, InscribeSerializerIn,ProfesorSerializer,AsignaturaSerializer,ImparteSerializer, SalonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class EstudianteView(APIView):
    def get(self,request):
        estudiantes = Estudiantes.objects.all()
        serializerE = EstudianteSerializer(estudiantes, many = True)
        return Response(serializerE.data)

    def post(self,request):
        serializerE = EstudianteSerializer(data = request.data)
        if serializerE.is_valid():
            serializerE.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerE.errors, status = status.HTTP_400_BAD_REQUEST)

class EstudianteDetalleView(APIView):
    def get(self,request,code):
        try:
            estudiantes = Estudiantes.objects.get(cod_e=code)
        except estudiantes.DoesNotExist:
            return Response({'error':'Estudiante No Encontrado...'}, status = status.HTTP_404_NOT_FOUND)
        serializerE = EstudianteSerializer(estudiantes)
        return Response(serializerE.data)
    
    def put(self,request,code):
        try:
            estudiantes = Estudiantes.objects.get(cod_e=code)
        except estudiantes.DoesNotExist:
            return Response({'error':'Estudiante No Encontrado...'}, status = status.HTTP_404_NOT_FOUND)
        serializerE = EstudianteSerializer(estudiantes,data = request.data)
        if serializerE.is_valid():
            serializerE.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerE.errors, status = status.HTTP_404_NOT_FOUND)
    def delete(self,request,code):
        try:
            estudiantes = Estudiantes.objects.get(cod_e=code)
        except estudiantes.DoesNotExist:
            return Response({'error':'Estudiante No Encontrado...'}, status = status.HTTP_404_NOT_FOUND)
        estudiantes.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
             


class CarreraView(APIView):
    def get(self,request):
        carreras = Carreras.objects.all()
        serializerC = CarreraSerializer(carreras, many = True)
        return Response(serializerC.data)
    def post(self,request):
        serializerC = CarreraSerializer(data = request.data)
        if serializerC.is_valid():
            serializerC.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerC.errors, status = status.HTTP_400_BAD_REQUEST)

class CarreraDetalleView(APIView):
    def get(self,request,id):
        try:
            carreras = Carreras.objects.get(id_carrera=id)
        except :
            return Response({'error':'Carrera No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerC = CarreraSerializer(carreras)
        return Response(serializerC.data)
    
    def put(self,request,id):
        try:
            carreras = Carreras.objects.get(id_carrera=id)
        except:
            return Response({'error':'Carrera No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerC = CarreraSerializer(carreras,data = request.data)
        if serializerC.is_valid():
            serializerC.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerC.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            carreras = Carreras.objects.get(id_carrera=id)
        except:
            return Response({'error':'Carrera No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        carreras.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)

class ProfesorView(APIView):
    def get(self,request):
        profesor = Profesor.objects.all()
        serializerProfesor = ProfesorSerializer(profesor, many = True)
        return Response(serializerProfesor.data)
    def post(self,request):
        serializerProfesor = ProfesorSerializer(data = request.data)
        if serializerProfesor.is_valid():
            serializerProfesor.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerProfesor.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfesorDetalleView(APIView):
    def get(self,request,cod):
        try:
            profesor = Profesor.objects.get(codProfesor=cod)
        except:
            return Response({'error':'Profesor No Encontrado...'}, status = status.HTTP_404_NOT_FOUND)
        serializerProfesor = ProfesorSerializer(profesor)
        return Response(serializerProfesor.data)
    
    def put(self,request,cod):
        try:
            profesor = Profesor.objects.get(codProfesor=cod)
        except:
            return Response({'error':'Profesor No Encontrado...'}, status = status.HTTP_404_NOT_FOUND)
        serializerProfesor = ProfesorSerializer(profesor,data = request.data)
        if serializerProfesor.is_valid():
            serializerProfesor.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerProfesor.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,cod):
        try:
            profesor = Profesor.objects.get(codProfesor=cod)
        except:
            return Response({'error':'Carrera No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        profesor.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)



class AsignaturaView(APIView):
    def get(self,request):
        asig = Asignatura.objects.all()
        serializerAsignatura = AsignaturaSerializer(asig, many = True)
        return Response(serializerAsignatura.data)

    def post(self,request):
        serializerAsignatura = AsignaturaSerializer(data = request.data)
        if serializerAsignatura.is_valid():
            serializerAsignatura.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerAsignatura.errors, status = status.HTTP_400_BAD_REQUEST)

class AsignaturaDetalleView(APIView):
    def get(self,request,code):
        try:
            asignatura = Asignatura.objects.get(cod_Asig=code)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerAsignatura = AsignaturaSerializer(asignatura)
        return Response(serializerAsignatura.data)
    
    def put(self,request,code):
        try:
            asignatura = Asignatura.objects.get(cod_Asig=code)
        except asignatura.DoesNotExist:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerAsignatura = AsignaturaSerializer(asignatura,data = request.data)
        if serializerAsignatura.is_valid():
            serializerAsignatura.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerAsignatura.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,code):
        try:
            asignatura = Asignatura.objects.get(cod_Asig=code)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        asignatura.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)

class ImparteView(APIView):
    def get(self,request):
        imparte = Imparte.objects.all()
        serializerImparte = ImparteSerializer(imparte, many = True)
        return Response(serializerImparte.data)

    def post(self,request):
        serializerImparte = ImparteSerializerIn(data = request.data)
        if serializerImparte.is_valid():
            serializerImparte.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerImparte.errors, status = status.HTTP_400_BAD_REQUEST)

class ImparteDetalleView(APIView):
    def get(self,request,cod):
        try:
            imparte = Imparte.objects.get(cod_imparte=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerImparte = ImparteSerializer(imparte)
        return Response(serializerImparte.data)
    
    def put(self,request,cod):
        try:
            imparte = Imparte.objects.get(cod_imparte=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerImparte = ImparteSerializer(imparte,data = request.data)
        if serializerImparte.is_valid():
            serializerImparte.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerImparte.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,cod):
        try:
            imparte = Imparte.objects.get(cod_imparte=cod)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        imparte.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)


class InscribeView(APIView):
    def get(self,request):
        inscribe = Inscribe.objects.all()
        serializerInscribe = InscribeSerializer(inscribe, many = True)
        return Response(serializerInscribe.data)
    
    def post(self,request):
        serializerInscribe = InscribeSerializerIn(data = request.data)      
        if serializerInscribe.is_valid():
            serializerInscribe.validated_data['definitiva'] = (serializerInscribe.validated_data['nota1']*0.35) + (serializerInscribe.validated_data['nota2']*0.35) + (serializerInscribe.validated_data['nota3']*0.3) 
            serializerInscribe.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerInscribe.errors, status = status.HTTP_400_BAD_REQUEST)

class InscribeDetalleView(APIView):


    def get(self,request,cod):
        try:
            inscribe = Inscribe.objects.get(cod_insc=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerInscribe = InscribeSerializer(inscribe)
        return Response(serializerInscribe.data)
    
    def put(self,request,cod):
        try:
            inscribe = Inscribe.objects.get(cod_insc=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerInscribe = InscribeSerializer(inscribe,data = request.data)
        if serializerInscribe.is_valid():
            serializerInscribe.validated_data['definitiva'] = (serializerInscribe.validated_data['nota1']*0.35) + (serializerInscribe.validated_data['nota2']*0.35) + (serializerInscribe.validated_data['nota3']*0.3)
            serializerInscribe.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerInscribe.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,cod):
        try:
            inscribe = Inscribe.objects.get(cod_insc=cod)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        inscribe.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)

class SalonView(APIView):
    def get(self,request):
        salon = Salon.objects.all()
        serializerSalon = SalonSerializer(salon, many = True)
        return Response(serializerSalon.data)

    def post(self,request):
        serializerSalon = SalonSerializer(data = request.data)
        if serializerSalon.is_valid():
            serializerSalon.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerSalon.errors, status = status.HTTP_400_BAD_REQUEST)

class SalonDetalleView(APIView):
    def get(self,request,cod):
        try:
            salon = Salon.objects.get(cod_salon=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerSalon = SalonSerializer(salon)
        return Response(serializerSalon.data)
    
    def put(self,request,cod):
        try:
            salon = Salon.objects.get(cod_salon=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerSalon = SalonSerializer(salon,data = request.data)
        if serializerSalon.is_valid():
            serializerSalon.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerSalon.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,cod):
        try:
            salon = Salon.objects.get(cod_salon=cod)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        salon.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)

class AsociadoView(APIView):
    def get(self,request):
        asociado = Asociado.objects.all()
        serializerAsociado = AsociadoSerializer(asociado, many = True)
        return Response(serializerAsociado.data)

    def post(self,request):
        serializerAsociado = AsociadoSerializerIn(data = request.data)
        if serializerAsociado.is_valid():
            serializerAsociado.save()
            return Response({'message':'Se Inserto el registro correctamente'}, status = status.HTTP_201_CREATED)
        else:
             return Response(serializerAsociado.errors, status = status.HTTP_400_BAD_REQUEST)

class AsociadoDetalleView(APIView):
    def get(self,request,cod):
        try:
            asociado = Asociado.objects.get(cod_asociado=cod)
        except:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerAsociado = AsociadoSerializer(asociado)
        return Response(serializerAsociado.data)
    
    def put(self,request,cod):
        try:
            asociado = Asociado.objects.get(cod_asociado=cod)
        except asociado.DoesNotExist:
            return Response({'error':'Informacion No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        serializerAsociado = AsociadoSerializer(asociado,data = request.data)
        if serializerAsociado.is_valid():
            serializerAsociado.save()
            return Response({'message':'Se Actualizo el registro correctamente'}, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializerAsociado.errors, status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,cod):
        try:
            asociado = Asociado.objects.get(cod_asociado=cod)
        except:
            return Response({'error':'Asignatura No Encontrada...'}, status = status.HTTP_404_NOT_FOUND)
        asociado.delete()
        return Response({'message':'Se Elimino el registro correctamente'}, status = status.HTTP_202_ACCEPTED)


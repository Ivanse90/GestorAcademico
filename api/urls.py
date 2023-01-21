from re import A
from django.urls import path
from .views import EstudianteView,CarreraView,ProfesorView,AsignaturaView,ImparteView,SalonView
from .views import AsociadoView,InscribeView,EstudianteDetalleView,CarreraDetalleView,ProfesorDetalleView,AsignaturaDetalleView
from .views import ImparteDetalleView,InscribeDetalleView,SalonDetalleView,AsociadoDetalleView
urlpatterns = [
    path('carreras/',CarreraView.as_view(),name='carreraslist'),
    path('estudiantes/',EstudianteView.as_view(),name='estudianteslist'),
    path('profesor/',ProfesorView.as_view(),name='ImpartePlist'),
    path('asignatura/',AsignaturaView.as_view(),name='imparteAList'),
    path('imparte/',ImparteView.as_view(),name='imparteList'),
    path('inscribe/',InscribeView.as_view(),name='inscribeList'),
    path('salon/',SalonView.as_view(),name='salonList'),
    path('asociado/',AsociadoView.as_view(),name='asociadoList'),
    path('asignatura/<int:code>',AsignaturaDetalleView.as_view(),name='asignaturas'),
    path('estudiantes/<int:code>',EstudianteDetalleView.as_view(),name='estudiante'),
    path('carreras/<int:id>',CarreraDetalleView.as_view(),name='carreras'),
    path('profesor/<int:cod>',ProfesorDetalleView.as_view(),name='profesor'),
    path('imparte/<str:cod>',ImparteDetalleView.as_view(),name='imparte'),
    path('inscribe/<int:cod>',InscribeDetalleView.as_view(),name='inscribe'),
    path('salon/<int:cod>',SalonDetalleView.as_view(),name='salon'),
    path('asociado/<str:cod>',AsociadoDetalleView.as_view(),name='salon'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.studyMasim, name='studyMasim'),
    path('Masim', views.studyMasim, name='studyMasim'),
    path('BurkinaFaso', views.studyBurkinaFaso, name = 'studyBurkinaFaso'),
    path('Masim/Insert', views.studyMasimInsert, name='studyMasimInsert'),
    #path('BurkinaFaso/Insert', views.studyBurkinaFasoInsert, name = 'studyBurkinaFasoInsert'),
]

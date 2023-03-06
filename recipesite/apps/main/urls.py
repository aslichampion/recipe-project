from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carousel', views.carousel, name='carousel'),
    path('test', views.test, name='test'),
]

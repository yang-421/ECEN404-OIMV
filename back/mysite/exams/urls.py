from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-quize/', views.addQuiz, name='addQuiz'),
]
"""Trainingz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from trainingz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('add_workout_block/', views.AddWorkoutBlockView.as_view(), name='add_workout_block'),
    path('list_workout_blocks/', views.ShowWorkoutBlocksView.as_view(), name='list_workout_blocks'),
    path('workout_block/<int:id>/', views.ShowDetailWorkoutBlockView.as_view(), name='detail_workout_block'),
    path('update_workout_block/<int:id>/', views.UpdateWorkoutBlockView.as_view(), name='update_workout_block'),
    path('delete_workout_block/<int:id>/', views.DeleteWorkoutBlockView.as_view(), name='delete_workout_block'),
    path('add_training_day/', views.AddTrainingDayView.as_view(), name='add_training_day'),
    path('list_training_days/', views.ShowTrainingDaysView.as_view(), name='list_training_days'),
    path('training_day/<int:id>/', views.ShowDetailTrainingDayView.as_view(), name='detail_training_day'),
    path('update_training_day/<int:id>/', views.UpdateWorkoutBlockView.as_view(), name='update_training_day'),
    path('delete_training_day/<int:id>/', views.DeleteWorkoutBlockView.as_view(), name='delete_training_day'),
    path('add_training_week/', views.AddTrainingWeekView.as_view(), name='add_training_week'),
    path('list_training_weeks/', views.ShowTrainingWeeksView.as_view(), name='list_training_weeks'),
]

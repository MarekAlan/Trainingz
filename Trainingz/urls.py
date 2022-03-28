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

]

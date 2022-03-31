from django.urls import path

from trainingz_app import views

urlpatterns = [
    path('add_workout_block/', views.AddWorkoutBlockView.as_view(), name='add_workout_block'),
    path('list_workout_blocks/', views.ShowWorkoutBlocksView.as_view(), name='list_workout_blocks'),
    path('workout_block/<int:id>/', views.ShowDetailWorkoutBlockView.as_view(), name='detail_workout_block'),
    path('update_workout_block/<int:id>/', views.UpdateWorkoutBlockView.as_view(), name='update_workout_block'),
    path('delete_workout_block/<int:id>/', views.DeleteWorkoutBlockView.as_view(), name='delete_workout_block'),
    path('add_training_day/', views.AddTrainingDayView.as_view(), name='add_training_day'),
    path('list_training_days/', views.ShowTrainingDaysView.as_view(), name='list_training_days'),
    path('training_day/<int:id>/', views.ShowDetailTrainingDayView.as_view(), name='detail_training_day'),
    path('update_training_day/<int:id>/', views.UpdateTrainingDayView.as_view(), name='update_training_day'),
    path('delete_training_day/<int:id>/', views.DeleteTrainingDay.as_view(), name='delete_training_day'),
    path('add_training_week/', views.AddTrainingWeekView.as_view(), name='add_training_week'),
    path('list_training_weeks/', views.ShowTrainingWeeksView.as_view(), name='list_training_weeks'),
    path('training_week/<int:id>/', views.ShowDetailTrainingWeekView.as_view(), name='detail_training_week'),
    path('update_training_week/<int:id>/', views.UpdateTrainingWeekView.as_view(), name='update_training_week'),
    path('delete_training_week/<int:id>/', views.DeleteTrainingWeek.as_view(), name='delete_training_week'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
]

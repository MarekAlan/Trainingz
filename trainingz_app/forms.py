from django import forms

from trainingz_app.models import WorkoutBlock, TrainingDay, TrainingWeek


class AddWorkoutBlockForm(forms.ModelForm):
    class Meta:
        model = WorkoutBlock
        fields = '__all__'


class AddTrainingDayForm(forms.ModelForm):
    class Meta:
        model = TrainingDay
        exclude = ['duration']


class AddTrainingWeekForm(forms.ModelForm):
    class Meta:
        model = TrainingWeek
        fields = '__all__'

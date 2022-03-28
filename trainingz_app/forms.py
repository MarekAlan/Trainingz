from django import forms

from trainingz_app.models import WorkoutBlock


class AddWorkoutBlockForm(forms.ModelForm):

    class Meta:
        model = WorkoutBlock
        fields = '__all__'
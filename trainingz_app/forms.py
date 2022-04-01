from django import forms
from django.forms import CheckboxSelectMultiple, DateInput

from trainingz_app.models import WorkoutBlock, Training, TrainingWeek, Comment


class AddWorkoutBlockForm(forms.ModelForm):
    class Meta:
        model = WorkoutBlock
        fields = "__all__"


class AddTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ["duration"]
        widgets = {
            'workout_blocks': CheckboxSelectMultiple,
            'date': DateInput(attrs={'type': 'date'})
        }


class AddWorkoutBlockToTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["workout_blocks"]
        widgets = {
            'workout_blocks': CheckboxSelectMultiple
        }


class AddTrainingWeekForm(forms.ModelForm):
    class Meta:
        model = TrainingWeek
        fields = "__all__"
        widgets = {
            'training_days': CheckboxSelectMultiple
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["author"]

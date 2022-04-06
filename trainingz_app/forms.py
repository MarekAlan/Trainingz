from django import forms
from django.forms import CheckboxSelectMultiple, DateInput

from trainingz_app.models import (
    WorkoutBlock,
    Training,
    TrainingWeek,
    Comment,
    TrainingDay, Activity,
)

class AddActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

class AddWorkoutBlockForm(forms.ModelForm):
    class Meta:
        model = WorkoutBlock
        fields = "__all__"


class AddTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ["duration"]
        widgets = {"workout_blocks": CheckboxSelectMultiple}


class AddWorkoutBlockToTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["workout_blocks"]
        widgets = {"workout_blocks": CheckboxSelectMultiple}


class AddTrainingWeekForm(forms.ModelForm):
    class Meta:
        model = TrainingWeek
        exclude = ["trainings"]
        widgets = {
            "start_date": DateInput(attrs={"type": "date"}),
            "end_date": DateInput(attrs={"type": "date"}),
        }


class AddTrainingDayForm(forms.ModelForm):
    class Meta:
        model = TrainingDay
        exclude = ["completed"]
        widgets = {"date": DateInput(attrs={"type": "date"})}


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

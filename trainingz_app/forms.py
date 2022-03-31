from django import forms

from trainingz_app.models import WorkoutBlock, TrainingDay, TrainingWeek, Comment


class AddWorkoutBlockForm(forms.ModelForm):
    class Meta:
        model = WorkoutBlock
        fields = '__all__'


class AddTrainingDayForm(forms.ModelForm):
    class Meta:
        model = TrainingDay
        exclude = ['duration']


class AddWorkoutBlockToTrainingDayForm(forms.ModelForm):
    class Meta:
        model = TrainingDay
        fields = ['workout_blocks']


class AddTrainingWeekForm(forms.ModelForm):
    class Meta:
        model = TrainingWeek
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']


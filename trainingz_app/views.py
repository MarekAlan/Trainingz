from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from trainingz_app.forms import AddWorkoutBlockForm, AddTrainingDayForm, AddTrainingWeekForm, AddCommentForm, \
    AddWorkoutBlockToTrainingDayForm
from trainingz_app.models import WorkoutBlock, TrainingDay, TrainingWeek


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AddWorkoutBlockView(View):

    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_workout_blocks')
        return render(request, 'form.html', {'form': form})


class ShowWorkoutBlocksView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': WorkoutBlock.objects.all()})


class ShowDetailWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, 'workout_block_detail.html', {'workout_block': workout_block})


class UpdateWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(instance=workout_block)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(request.POST, instance=workout_block)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_workout_block', args=[id]))
        return render(request, 'form.html', {'form': form})

class DeleteWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        workout_block.delete()
        return redirect('list_workout_blocks')


class AddTrainingDayView(View):

    def get(self, request):
        form = AddTrainingDayForm()
        return render(request, 'form.html', {'form': form})


    def post(self, request):
        form = AddTrainingDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_training_days')
        return render(request, 'form.html', {'form': form})

class ShowTrainingDaysView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': TrainingDay.objects.all()})


class ShowDetailTrainingDayView(View):

    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        form = AddWorkoutBlockToTrainingDayForm()
        ctx = {
            'training_day': training_day,
            'form': form
        }
        return render(request, 'training_day_detail.html', ctx)

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        form = AddWorkoutBlockToTrainingDayForm(request.POST)
        workout_block = request.POST['workout_blocks']
        training_day.workout_blocks.add(workout_block)
        return redirect(f'/trainingz_app/training_day/{training_day.id}')


class UpdateTrainingDayView(View):

    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        form = AddTrainingDayForm(instance=training_day)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        form = AddTrainingDayForm(request.POST, instance=training_day)
        if form.is_valid():
            form.save()
            return redirect(f'/trainingz_app/training_day/{training_day.id}')
        return render(request, 'form.html', {'form': form})


class DeleteTrainingDay(View):

    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        return render(request, 'form.html')

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_day.delete()
        return redirect('list_training_days')


class AddTrainingWeekView(View):

    def get(self, request):
        form = AddTrainingWeekForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddTrainingWeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_training_week')
        return render(request, 'form.html', {'form': form})


class ShowTrainingWeeksView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': TrainingWeek.objects.all()})


class ShowDetailTrainingWeekView(View):

    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        training_days = training_week.training_days.all()
        return render(request, 'training_week_detail.html', {'training_week': training_week, 'training_days': training_days})


class UpdateTrainingWeekView(View):

    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        form = AddTrainingWeekForm(instance=training_week)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        form = AddTrainingWeekForm(request.POST, instance=training_week)
        if form.is_valid():
            form.save()
            return redirect(f'/trainingz_app/training_week/{training_week.id}')
        return render(request, 'form.html', {'form': form})


class DeleteTrainingWeek(View):

    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        return render(request, 'form.html')

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        training_week.delete()
        return redirect('list_training_weeks')


class AddCommentView(View):

    def get(self, request):
        form = AddCommentForm()
        return render(request, 'form.html')

    def post(self, request):
        form = AddCommentForm(request.POST, instance=TrainingDay)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('detail_training_day')
        return render(request, 'form.html', {'form': form})
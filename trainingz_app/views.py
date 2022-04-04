from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from trainingz_app.forms import (
    AddWorkoutBlockForm,
    AddTrainingForm,
    AddTrainingWeekForm,
    AddCommentForm,
    AddWorkoutBlockToTrainingForm, AddTrainingDayForm,
)
from trainingz_app.models import WorkoutBlock, Training, TrainingWeek, TrainingDay, Comment


class IndexView(View):
    def get(self, request):
        return render(request, "base.html")


class AddWorkoutBlockView(View):
    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_workout_blocks")
        return render(request, "form.html", {"form": form})


class ShowWorkoutBlocksView(View):
    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(request, "list_workout_blocks.html", {"object_list": WorkoutBlock.objects.all(), 'form': form})

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_workout_blocks")

class ShowDetailWorkoutBlockView(View):
    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(
            request, "workout_block_detail.html", {"workout_block": workout_block}
        )


class UpdateWorkoutBlockView(View):
    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(instance=workout_block)
        return render(request, "form.html", {"form": form})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(request.POST, instance=workout_block)
        if form.is_valid():
            form.save()
            return redirect(reverse("detail_workout_block", args=[id]))
        return render(request, "form.html", {"form": form})


class DeleteWorkoutBlockView(View):
    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, "form.html", {})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        workout_block.delete()
        return redirect("list_workout_blocks")


class AddTrainingView(View):
    def get(self, request):
        form = AddTrainingForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = AddTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_trainings")
        return render(request, "form.html", {"form": form})


class ShowTrainingsView(View):
    def get(self, request):
        form = AddTrainingForm()
        return render(request, "list_trainings.html", {"object_list": Training.objects.all(), 'form': form})

    def post(self, request):
        form = AddTrainingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_trainings")


class ShowDetailTrainingView(View):
    def get(self, request, id):
        training = Training.objects.get(pk=id)
        workout_blocks = training.workout_blocks.all()
        training_duration = 0
        for workout_block in workout_blocks:
            training_duration += workout_block.duration
        form = AddWorkoutBlockToTrainingForm()
        ctx = {"training": training, "form": form, "training_duration": training_duration}
        return render(request, "training_detail.html", ctx)

    def post(self, request, id):
        training = Training.objects.get(pk=id)
        form = AddWorkoutBlockToTrainingForm(request.POST)
        workout_block = request.POST["workout_blocks"]
        training.workout_blocks.add(workout_block)
        return redirect(f"/trainingz_app/training/{training.id}")


class UpdateTrainingView(View):
    def get(self, request, id):
        training = Training.objects.get(pk=id)
        form = AddTrainingForm(instance=training)
        return render(request, "form.html", {"form": form})

    def post(self, request, id):
        training = Training.objects.get(pk=id)
        form = AddTrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect(f"/trainingz_app/training/{training.id}")
        return render(request, "form.html", {"form": form})


class DeleteTraining(View):
    def get(self, request, id):
        training = Training.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training = Training.objects.get(pk=id)
        training.delete()
        return redirect("list_trainings")


class AddTrainingWeekView(View):
    def get(self, request):
        form_week = AddTrainingWeekForm()
        return render(request, "form_training_week.html", {"form_week": form_week})

    def post(self, request):
        form_week = AddTrainingWeekForm(request.POST)
        if form_week.is_valid():
            form_week.save()
            return redirect("list_training_weeks")
        return render(request, "form_training_week.html", {"form_week": form_week})



class ShowTrainingWeeksView(View):
    def get(self, request):
        return render(request, "list_training_weeks.html", {"object_list": TrainingWeek.objects.all()})


class ShowDetailTrainingWeekView(View):
    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        trainings = training_week.trainings.all().order_by('date')
        form_training = AddTrainingDayForm()
        return render(
            request,
            "training_week_detail.html",
            {"training_week": training_week, "trainings": trainings, 'form_training': form_training},
        )

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        trainings = training_week.trainings.all()
        form_training = AddTrainingDayForm(request.POST)
        if form_training.is_valid():
            training = form_training.cleaned_data['training']
            date = form_training.cleaned_data['date']
            training_day = TrainingDay.objects.create(training=training, date=date)
            training_week.trainings.add(training_day)
            training_week.save()
        return render(
            request,
            "training_week_detail.html",
            {"training_week": training_week, "trainings": trainings,  'form_training': form_training},
        )


class UpdateTrainingWeekView(View):
    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        form = AddTrainingWeekForm(instance=training_week)
        return render(request, "form.html", {"form": form})

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        form = AddTrainingWeekForm(request.POST, instance=training_week)
        if form.is_valid():
            form.save()
            return redirect(f"/trainingz_app/training_week/{training_week.id}")
        return render(request, "form.html", {"form": form})


class DeleteTrainingWeek(View):
    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        training_week.delete()
        return redirect("list_training_weeks")


class ShowDetailTrainingDayView(View):
    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_id = TrainingDay.objects.get(pk=id).training_id
        training = Training.objects.get(pk=training_id)
        workout_blocks = training.workout_blocks.all()
        comments = training_day.comment_set.all()
        form = AddCommentForm()
        training_duration = 0
        for workout_block in workout_blocks:
            training_duration += workout_block.duration
        ctx = {'comments': comments, "form": form, "training": training, "training_duration": training_duration, 'training_day': training_day}
        return render(request, "training_day_detail.html", ctx)

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_id = TrainingDay.objects.get(pk=id).training_id
        training = Training.objects.get(pk=training_id)
        workout_blocks = training.workout_blocks.all()
        comments = training_day.comment_set.all()
        training_duration = 0
        for workout_block in workout_blocks:
            training_duration += workout_block.duration
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.training_day = training_day
            comment.save()
        ctx = {'comments': comments, "form": form, "training": training, "training_duration": training_duration,
               'training_day': training_day}
        return render(request, "training_day_detail.html", ctx)

class DeleteTrainingDay(View):
    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_day.delete()
        return redirect("list_training_weeks")


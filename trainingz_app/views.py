from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from trainingz_app.forms import (
    AddWorkoutBlockForm,
    AddTrainingForm,
    AddTrainingWeekForm,
    AddCommentForm,
    AddWorkoutBlockToTrainingForm,
)
from trainingz_app.models import WorkoutBlock, Training, TrainingWeek


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
        form = AddTrainingWeekForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = AddTrainingWeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_training_weeks")
        return render(request, "form.html", {"form": form})


class ShowTrainingWeeksView(View):
    def get(self, request):
        return render(request, "list_workout_blocks.html", {"object_list": TrainingWeek.objects.all()})


class ShowDetailTrainingWeekView(View):
    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        trainings = training_week.training_days.all()
        return render(
            request,
            "training_week_detail.html",
            {"training_week": training_week, "trainings": trainings},
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


class AddCommentView(View):
    def get(self, request):
        form = AddCommentForm()
        return render(request, "form.html")

    def post(self, request):
        form = AddCommentForm(request.POST, instance=Training)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect("detail_training")
        return render(request, "form.html", {"form": form})

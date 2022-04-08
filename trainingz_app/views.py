from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
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
    AddTrainingDayForm, AddActivityForm,
)
from trainingz_app.models import (
    WorkoutBlock,
    Training,
    TrainingWeek,
    TrainingDay,
    Comment, Activity,
)


class IndexView(View):
    """
    Returns homepage.
    """

    def get(self, request):
        return render(request, "base.html")

class ShowActivitiesView(LoginRequiredMixin, View):
    """
    Add an activity and shows a list of them
    """

    def get(self, request):
        form = AddActivityForm()
        return render(
            request,
            "list_activites.html",
            {"object_list": Activity.objects.all(), "form": form},
        )

    def post(self, request):
        form = AddActivityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_activities")


class AddWorkoutBlockView(LoginRequiredMixin, View):
    """
    Add a single workout block
    """

    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_workout_blocks")
        return render(request, "form.html", {"form": form})


class ShowWorkoutBlocksView(LoginRequiredMixin, View):
    """
    List of workout blocks added.
    """

    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(
            request,
            "list_workout_blocks.html",
            {"object_list": WorkoutBlock.objects.all(), "form": form},
        )

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_workout_blocks")


class ShowDetailWorkoutBlockView(LoginRequiredMixin, View):
    """
    Show detailas of a workout block
    """

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(
            request, "workout_block_detail.html", {"workout_block": workout_block}
        )


class UpdateWorkoutBlockView(LoginRequiredMixin, View):
    """
    Uptades a workout block
    """

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


class DeleteWorkoutBlockView(LoginRequiredMixin, View):
    """
    Deletes a workout block
    """

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, "form.html", {})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        workout_block.delete()
        return redirect("list_workout_blocks")


class AddTrainingView(LoginRequiredMixin, View):
    """
    Adds a single training made of many workout blocks
    """

    def get(self, request):
        form = AddTrainingForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = AddTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_trainings")
        return render(request, "form.html", {"form": form})


class ShowTrainingsView(LoginRequiredMixin, View):
    """
    Lists of all trainings
    """

    def get(self, request):
        form = AddTrainingForm()
        return render(
            request,
            "list_trainings.html",
            {"object_list": Training.objects.all(), "form": form},
        )

    def post(self, request):
        form = AddTrainingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_trainings")


class ShowDetailTrainingView(LoginRequiredMixin, View):
    """
    Details of an single workout
    """

    def get(self, request, id):
        training = Training.objects.get(pk=id)
        workout_blocks = training.workout_blocks.all()
        training_duration = 0
        for workout_block in workout_blocks:
            training_duration += workout_block.duration
        form = AddWorkoutBlockToTrainingForm()
        ctx = {
            "training": training,
            "form": form,
            "training_duration": training_duration,
        }
        return render(request, "training_detail.html", ctx)

    def post(self, request, id):
        training = Training.objects.get(pk=id)
        form = AddWorkoutBlockToTrainingForm(request.POST)
        workout_block = request.POST["workout_blocks"]
        training.workout_blocks.add(workout_block)
        return redirect(f"/trainingz_app/training/{training.id}")


class UpdateTrainingView(LoginRequiredMixin, View):
    """
    Updates a single training
    """

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


class DeleteTraining(LoginRequiredMixin, View):
    """
    Delets a specific training
    """

    def get(self, request, id):
        training = Training.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training = Training.objects.get(pk=id)
        training.delete()
        return redirect("list_trainings")


class AddTrainingWeekView(LoginRequiredMixin, View):
    """ "
    Adds a Training Week
    """

    def get(self, request):
        form_week = AddTrainingWeekForm()
        return render(request, "form_training_week.html", {"form_week": form_week})

    def post(self, request):
        form_week = AddTrainingWeekForm(request.POST)
        if form_week.is_valid():
            form_week.save()
            return redirect("list_training_weeks")
        return render(request, "form_training_week.html", {"form_week": form_week})


class ShowTrainingWeeksView(LoginRequiredMixin, View):
    """
    Shows a list of all training weeeks
    """

    def get(self, request):
        form_week = AddTrainingWeekForm()
        return render(
            request,
            "list_training_weeks.html",
            {"object_list": TrainingWeek.objects.all(), "form_week": form_week},
        )

    def post(self, request):
        form_week = AddTrainingWeekForm(request.POST)
        if form_week.is_valid():
            form_week.save()
        return render(
            request,
            "list_training_weeks.html",
            {"object_list": TrainingWeek.objects.all(), "form_week": form_week},
        )


class ShowDetailTrainingWeekView(LoginRequiredMixin, View):
    """
    Shows details of a specific Training Week. It is also possible to add Training Days to this week
    """

    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        trainings = training_week.trainings.all().order_by("date")
        dates = TrainingDay.objects.dates('date', 'day')
        date_now = datetime.now()
        form_training = AddTrainingDayForm()
        return render(
            request,
            "training_week_detail.html",
            {
                "training_week": training_week,
                "trainings": trainings,
                "form_training": form_training,
                "dates": dates,
                "date_now": date_now,
            },
        )

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        trainings = training_week.trainings.all()
        form_training = AddTrainingDayForm(request.POST)
        if form_training.is_valid():
            training = form_training.cleaned_data["training"]
            date = form_training.cleaned_data["date"]
            training_day = TrainingDay.objects.create(training=training, date=date)
            training_week.trainings.add(training_day)
            training_week.save()
        return render(
            request,
            "training_week_detail.html",
            {
                "training_week": training_week,
                "trainings": trainings,
                "form_training": form_training,
            },
        )


class UpdateTrainingWeekView(LoginRequiredMixin, View):
    """
    Updates a specific Training Week
    """

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


class DeleteTrainingWeek(LoginRequiredMixin, View):
    """
    Deletes a specific Training Week
    """

    def get(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training_week = TrainingWeek.objects.get(pk=id)
        training_week.delete()
        return redirect("list_training_weeks")


class ShowDetailTrainingDayView(LoginRequiredMixin, View):
    """
    Shows details of a Training Day. Allows to add comments by logged users
    """

    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_id = TrainingDay.objects.get(pk=id).training_id
        training = Training.objects.get(pk=training_id)
        workout_blocks = training.workout_blocks.all()
        comments = training_day.comment_set.all()
        form = AddCommentForm()
        # form_training_completed = TrainingDayCompletedForm()
        training_duration = 0
        for workout_block in workout_blocks:
            training_duration += workout_block.duration
        ctx = {
            "comments": comments,
            "form": form,
            "training": training,
            "training_duration": training_duration,
            "training_day": training_day,
        }
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
        ctx = {
            "comments": comments,
            "form": form,
            "training": training,
            "training_duration": training_duration,
            "training_day": training_day,
        }
        if "add_comment" in request.POST:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.training_day = training_day
                comment.save()
            return render(request, "training_day_detail.html", ctx)
        completed = request.POST["Completed"]
        training_day.completed = completed
        training_day.save()
        return render(request, "training_day_detail.html", ctx)


class DeleteTrainingDay(LoginRequiredMixin, View):
    """
    Deletes a Training Day
    """

    def get(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        return render(request, "form.html")

    def post(self, request, id):
        training_day = TrainingDay.objects.get(pk=id)
        training_day.delete()
        return redirect("list_training_weeks")

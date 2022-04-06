import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse



class Activity(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


WORKOUT_ELEMENTS = (
    ("Warm Up", "Warm Up"),
    ("Active", "Active"),
    ("Cool Down", "Cool Down"),
)


class WorkoutBlock(models.Model):
    name = models.CharField(max_length=50)
    workout_element = models.CharField(max_length=30, choices=WORKOUT_ELEMENTS)
    workout_details = models.TextField()
    duration = models.SmallIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_workout_block", args=(self.id,))

    def get_update_url(self):
        return reverse("update_workout_block", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("delete_workout_block", kwargs={"id": self.id})


class Training(models.Model):
    name = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    workout_blocks = models.ManyToManyField(WorkoutBlock)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_training", args=(self.id,))

    def get_update_url(self):
        return reverse("update_training", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("delete_training", kwargs={"id": self.id})


TO_DO_COMPLETED = (("To Do", "To Do"), ("Completed", "Completed"))


class TrainingDay(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.CharField(
        max_length=15, choices=TO_DO_COMPLETED, default="To Do"
    )

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse("detail_training_day", args=(self.id,))

    def get_update_url(self):
        return reverse("update_training_day", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("delete_training_day", kwargs={"id": self.id})


class TrainingWeek(models.Model):
    name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    trainings = models.ManyToManyField(TrainingDay)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_training_week", args=(self.id,))

    def get_update_url(self):
        return reverse("update_training_week", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("delete_training_week", kwargs={"id": self.id})


class Comment(models.Model):
    training_day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

CHOICES = (
    ("Bike", "Road Bike"),
    ("MTB", "MTB"),
    ("Run", "Running"),
    ("Stretching", "Stretching"),
    ("Crosstrain", "Cross-Training"),
    ("Rest Day", "Rest Day"),
    ("Event", "Event"),
)


class Activity(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, choices=CHOICES)


DAYS = (
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday"),
)


class DayName(models.Model):
    name = models.CharField(max_length=3, choices=DAYS)
    order = models.SmallIntegerField(unique=True)

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


class TrainingDay(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse("detail_trainingday", args=(self.id,))

    def get_update_url(self):
        return reverse("update_trainingday", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("delete_trainingday", kwargs={"id": self.id})

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
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

CHOICES = (
    ('Bike', 'Road Bike'),
    ('MTB', 'MTB'),
    ('Run', 'Running'),
    ('Stretching', 'Stretching'),
    ('Crosstrain', 'Cross-Training'),
    ('Rest Day', 'Rest Day'),
    ('Event', 'Event'),
)


class Activity(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, choices=CHOICES)


DAYS = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday')
)


class DayName(models.Model):
    name = models.CharField(max_length=3, choices=DAYS)
    order = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.name


class WorkoutBlock(models.Model):
    name = models.CharField(max_length=50)
    workout_details = models.TextField()
    duration = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_workout_block",
                       args=(self.id,))

    def get_update_url(self):
        return reverse("update_workout_block", kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse("delete_workout_block", kwargs={'id': self.id})


WORKOUT_ELEMENTS = (
    ('Warm Up', 'Warm Up'),
    ('Active', 'Active'),
    ('Cool Down', 'Cool Down')
)


class TrainingDay(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    workout_element = models.CharField(max_length=30, choices=WORKOUT_ELEMENTS)
    workout_block = models.ManyToManyField(WorkoutBlock)
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
    duration = models.TimeField()

    def __str__(self):
        return self.workout_element


class TrainingWeek(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    training_days = models.ManyToManyField(TrainingDay)

    def __str__(self):
        return self.name


class Comment(models.Model):
    training_day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

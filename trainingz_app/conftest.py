import datetime

import pytest
from django.contrib.auth.models import User

from trainingz_app.models import WorkoutBlock, Activity, Training, TrainingWeek


@pytest.fixture
def users():
    users = []
    for x in range(10):
        u = User.objects.create(username=x)
        users.append(u)
    return users


@pytest.fixture
def user():
    return User.objects.create(username='yoda')


@pytest.fixture
def activities():
    activities = []
    lists = ["Bike", "MTB", "Run"]
    for item in lists:
        a = Activity.objects.create(name = item)
        activities.append(a)
    return activities


@pytest.fixture
def workout_blocks():
    workout_blocks = []
    for x in range(3):
        w = WorkoutBlock.objects.create(
            name='x', workout_element='x', workout_details='x', duration=1
        )
        workout_blocks.append(w)
    return workout_blocks


@pytest.fixture
def trainings(activities):
    trainings = []
    for activity in activities:
        for x in range(3):
            t = Training.objects.create(
                 name='x', activity=activity, description='x'
            )
            trainings.append(t)
    return trainings


@pytest.fixture
def training_weeks():
    training_weeks = []
    for x in range(3):
        t = TrainingWeek.objects.create(
            name='x', start_date=datetime.date.today(), end_date=datetime.date.today(), description='x'
        )
        training_weeks.append(t)
    return training_weeks



import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from trainingz_app.models import Comment


@pytest.mark.django_db
def test_check_index():
    client = Client()
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_workout_blocks_list(workout_blocks, user):
    client = Client()
    client.force_login(user)
    url = reverse("list_workout_blocks")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object_list"].count() == len(workout_blocks)
    for workout_block in workout_blocks:
        assert workout_block in response.context["object_list"]


@pytest.mark.django_db
def test_trainings_list(trainings, user):
    client = Client()
    client.force_login(user)
    url = reverse("list_trainings")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object_list"].count() == len(trainings)
    for training in trainings:
        assert training in response.context["object_list"]


@pytest.mark.django_db
def test_training_weeks_list(training_weeks, user):
    client = Client()
    client.force_login(user)
    url = reverse("list_training_weeks")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object_list"].count() == len(training_weeks)
    for training_week in training_weeks:
        assert training_week in response.context["object_list"]


@pytest.mark.django_db
def test_register_user():
    url = reverse("register")
    client = Client()
    d = {"username": "alan", "pass1": "bb", "pass2": "bb"}
    response = client.post(url, d)
    assert response.status_code == 302
    User.objects.get(username="alan")
    assert client.login(username="alan", password="bb")


@pytest.mark.django_db
def test_check_workout_block_add_get_not_login():
    client = Client()
    url = reverse("add_workout_block")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_workout_block(user):
    url = reverse("add_workout_block")
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_check_training_weeks_not_login():
    client = Client()
    url = reverse("list_training_weeks")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_check_training_weeks(user):
    url = reverse("list_training_weeks")
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_check_trainings_not_login():
    client = Client()
    url = reverse("list_trainings")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_check_trainings(user):
    url = reverse("list_trainings")
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200

# Generated by Django 4.0.3 on 2022-04-03 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Bike', 'Road Bike'), ('MTB', 'MTB'), ('Run', 'Running'), ('Stretching', 'Stretching'), ('Crosstrain', 'Cross-Training'), ('Rest Day', 'Rest Day'), ('Event', 'Event')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DayName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=3)),
                ('order', models.SmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainingz_app.activity')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainingz_app.training')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('workout_element', models.CharField(choices=[('Warm Up', 'Warm Up'), ('Active', 'Active'), ('Cool Down', 'Cool Down')], max_length=30)),
                ('workout_details', models.TextField()),
                ('duration', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('trainings', models.ManyToManyField(to='trainingz_app.trainingday')),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='workout_blocks',
            field=models.ManyToManyField(to='trainingz_app.workoutblock'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainingz_app.training')),
            ],
        ),
    ]

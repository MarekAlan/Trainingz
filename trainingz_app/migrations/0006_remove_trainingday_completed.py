# Generated by Django 4.0.3 on 2022-04-05 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingz_app', '0005_trainingday_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingday',
            name='completed',
        ),
    ]
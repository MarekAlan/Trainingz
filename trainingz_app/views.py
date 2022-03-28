from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from trainingz_app.forms import AddWorkoutBlockForm
from trainingz_app.models import WorkoutBlock


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AddWorkoutBlockView(View):

    def get(self, request):
        form = AddWorkoutBlockForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddWorkoutBlockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            workout_details = form.cleaned_data['workout_details']
            duration = form.cleaned_data['duration']
            description = form.cleaned_data['description']
            WorkoutBlock.objects.create(
                name=name,
                workout_details=workout_details,
                duration=duration,
                description=description)
            return redirect('list_workout_blocks')
        return render(request, 'form.html', {'form': form})


class ShowWorkoutBlocksView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': WorkoutBlock.objects.all()})


class ShowDetailWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, 'workout_block_detail.html', {'workout_block': workout_block})


class UpdateWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(instance=workout_block)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        form = AddWorkoutBlockForm(request.POST, instance=workout_block)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_workout_block', args=[id]))
        return render(request, 'form.html', {'form': form})

class DeleteWorkoutBlockView(View):

    def get(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        workout_block = WorkoutBlock.objects.get(pk=id)
        workout_block.delete()
        return redirect('list_workout_blocks')






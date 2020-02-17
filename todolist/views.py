from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            if List.objects.filter(task_name__iexact=form.cleaned_data['task_name']).exists():
                messages.error(request, "The task is already added to list!")
                return redirect("home")
            form.save()
            all_tasks = List.objects.all()
            context = {'all_tasks':all_tasks}
            messages.success(request,"New task added succesfully!")
            return render(request, 'home.html', context)
    else:
        all_tasks = List.objects.all()
        context = {'all_tasks':all_tasks}
        return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)


def delete(request,list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, "A task has been deleted!")
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == "POST":
        task = List.objects.get(pk = list_id)
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "A task has been edited!")
            return redirect('home')
    else:
        task = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'task':task})

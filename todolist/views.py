from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
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

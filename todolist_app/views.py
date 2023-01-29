from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasklist
from .form import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist_app')
    else:
        all_tasks = Tasklist.objects.all
        return render(request, 'todolist.html', {'all_tasks' : all_tasks})


def contact(request):
    context = {
        "contact_text": "Welcome ContactUs Page",
    }
    return render(request, 'contactus.html', context)


def about(request):
    context = {
        "about_text": "Welcome Aboutus Page",
    }
    return render(request, 'aboutus.html', context)

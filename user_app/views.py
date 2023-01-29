from django.shortcuts import render, redirect
from .forms import CustomRegisterationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created!"))
            return redirect('todolist')
    else:
        register_form = CustomRegisterationForm

    return render(request, 'register.html', {'register_form' : register_form})

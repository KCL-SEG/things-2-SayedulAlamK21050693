from django.shortcuts import render, redirect
from .forms import ThingForm

def home(request):
    if request.POST:
        form = ThingForm(request.POST)

        if form.is_valid():
            form.save()

    form = ThingForm()
    return render(request, 'home.html', {'form': form})

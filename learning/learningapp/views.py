from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def registration(request):
    form = UserForm()
    return render(request, "registration.html", {'form':form})
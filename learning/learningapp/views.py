from django.shortcuts import render
from .forms import UserForm,UserDetailsForm

# Create your views here.
def registration(request):
    form1 = UserForm()
    form2 = UserDetailsForm()
    return render(request, "registration.html", {'form1':form1,'form2':form2})

def add_details(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            pass
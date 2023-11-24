from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from Job_Portal.resume.models import Resume


# Create your views here.

# register applicants only
def register_applicants(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your Account has been created successfully.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong.')
            return request('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return redirect(request, 'users/register_applicant.html')

# register recruiter only


from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('/login/')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/jobs/')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_detail.html', {'job': job})

from .forms import ApplicationForm
from .models import Application

def apply_job(request, id):
    job = Job.objects.get(id=id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('/jobs/')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form, 'job': job})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': applications})

from django.contrib.auth import logout
def user_logout(request):
    logout(request)
    return redirect('/login/')

def home(request):
    return render(request, 'home.html')





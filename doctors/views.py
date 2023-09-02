from django.shortcuts import render
from .forms import DoctorForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users, admin_only, unauthenticated_user
from django.shortcuts import render, redirect, get_object_or_404
from .models import DoctorModel
from accounts.models import UserProfile
from accounts.forms import UserForm, UserProfileForm
from django.contrib import messages, auth
from .forms import DoctorForm

# Create your views here.
def doctors(request):
    doctors = DoctorModel.objects.all().order_by('-date_joined')
    is_doctor = False
    if request.user.is_authenticated:
        is_doctor = DoctorModel.objects.filter(account=request.user).exists()

    return render(request, 'doctors/doctors_list.html', {'doctors' : doctors, 'is_doctor': is_doctor})




@login_required(login_url='login')
def doctor_profile(request):
    doctor = DoctorModel.objects.get(account=request.user)
    doctor_form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
        else: 
            redirect('dashboard')

    return render(request, 'doctors/doctor_profile.html', {'doctor_form': doctor_form, 'doctor': doctor})
    

@login_required(login_url='login')
def doctor_register(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.account = request.user
            doctor.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
        else: 
            redirect('dashboard')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_register.html', {'form': form})
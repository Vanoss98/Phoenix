from django.shortcuts import redirect, render
from .forms import PatientCreationForm, RegularCreationForm, UserUpadteForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@csrf_exempt
def regular_register(request):
    if request.method == 'POST':
        form = RegularCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = RegularCreationForm()
    return render(request, 'Users/register.html', {'form':form})


@csrf_exempt
def patient_register(request):
    if request.method == 'POST':
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = PatientCreationForm()
    return render(request, 'Users/patient-register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpadteForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'تغییرات حساب کاربری اعمال')
            return redirect('profile')
    else:
        u_form = UserUpadteForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'Users/profile.html', context)
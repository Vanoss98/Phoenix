from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.template.defaultfilters import slugify
from .forms import DarmanServiceForm, BaztavaniServiceForm, GholakServiceForm, PishgiriServiceForm, KargahServiceForm, MoshavereServiceForm, MadadKariServiceForm, KaryabiForm, EstekhdamForm
from .models import Namayande, Pezashkan, Marakez


def darman_service_form(request):
    if request.method == 'POST':
        form = DarmanServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Darman-serv-page')
    else:
        form = DarmanServiceForm()
    return render(request, 'Services/darman-service.html', {'form': form})


def baztavani_service_form(request):
    if request.method == 'POST':
        form = BaztavaniServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Baztavani-serv-page')
    else:
        form = BaztavaniServiceForm()
    return render(request, 'Services/baztavani-service.html', {'form': form})


def pishgiri_service_form(request):
    if request.method == 'POST':
        form = PishgiriServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Pishgiri-serv-page')
    else:
        form = PishgiriServiceForm()
    return render(request, 'Services/pishgiri-service.html', {'form': form})


def kargah_service_form(request):
    if request.method == 'POST':
        form = KargahServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Kargah-serv-page')
    else:
        form = KargahServiceForm()
    return render(request, 'Services/kargah-service.html', {'form': form})


def moshavere_service_form(request):
    if request.method == 'POST':
        form = MoshavereServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Moshavere-serv-page')
    else:
        form = MoshavereServiceForm()
    return render(request, 'Services/moshavere-service.html', {'form': form})


def madadkari_service_form(request):

    if request.method == 'POST':
        form = MadadKariServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Madadkari-serv-page')
    else:
        form = MadadKariServiceForm()
    return render(request, 'Services/madadkari-service.html', {'form': form})


def gholak_service_form(request):

    if request.method == 'POST':
        form = GholakServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Gholak-page')
    else:
        form = GholakServiceForm()
    return render(request, 'Services/gholak.html', {'form': form})


def nmp_view(request):
    namayande = Namayande.objects.all()
    marakez = Marakez.objects.all()
    pezeshkan = Pezashkan.objects.all()
    context = {
        'namayande':namayande,
        'marakez':marakez,
        'pezeshkan':pezeshkan,
    }
    return render(request, 'Services/npm.html', context)



def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

class MyView(TemplateView):
    template_name = 'Services/karyabi.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'aform': KaryabiForm(prefix='aform_pre'), 'bform': EstekhdamForm(prefix='bform_pre')})

    def post(self, request, *args, **kwargs):
        aform = _get_form(request, KaryabiForm, 'aform_pre')
        bform = _get_form(request, EstekhdamForm, 'bform_pre')
        if aform.is_bound and aform.is_valid():
            messages.success(request, f'فرم با موفقیت ثبت شد')
            aform.save()
            return redirect('Karyabi-page')
        elif bform.is_bound and bform.is_valid():
            messages.success(request, f'فرم با موفقیت ثبت شد')
            bform.save()
            return redirect('Karyabi-page')
        return self.render_to_response({'aform': aform, 'bform': bform})
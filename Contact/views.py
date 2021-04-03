from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, HelpForm
from django.views.generic import TemplateView


class helpView(TemplateView):
    template_name = 'Contact/help-main.html'


def help_form(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Help-form-page')
    else:
        form = HelpForm()
    return render(request, 'Contact/help-detail.html', {'form': form})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Contact-page')
    else:
        form = ContactForm()
    return render(request, 'Contact/contact.html', {'form': form})

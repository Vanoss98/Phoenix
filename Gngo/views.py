from Gngo.models import Campaign, CampaignImages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.core.paginator import Paginator
from taggit.models import Tag
from django.template.defaultfilters import slugify
from .forms import DarmanForm, PishgiriForm, BaztavaniForm, RavabetOmumiForm, KhayerinForm


class aboutPage(TemplateView):
    template_name = 'Gngo/about.html'


class maramnamePage(TemplateView):
    template_name = 'Gngo/maramname.html'


class ketabchePage(TemplateView):
    template_name = 'Gngo/ketabche.html'


def pishgiri_form(request):
    if request.method == 'POST':
        form = PishgiriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Pishgiri-page')
    else:
        form = PishgiriForm()
    return render(request, 'Gngo/pishgiri.html', {'form': form})


def darman_form(request):
    if request.method == 'POST':
        form = DarmanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Darman-page')
    else:
        form = PishgiriForm()
    return render(request, 'Gngo/darman.html', {'form': form})


def baztavani_form(request):
    if request.method == 'POST':
        form = BaztavaniForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Baztavani-page')
    else:
        form = BaztavaniForm()
    return render(request, 'Gngo/baztavani.html', {'form': form})


def ravabet_form(request):
    if request.method == 'POST':
        form = RavabetOmumiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Ravabet-page')
    else:
        form = RavabetOmumiForm()
    return render(request, 'Gngo/ravabet.html', {'form': form})


def khayerin_form(request):
    if request.method == 'POST':
        form = KhayerinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'فرم با موفقیت ثبت شد')
            return redirect('Khayerin-page')
    else:
        form = KhayerinForm()
    return render(request, 'Gngo/khayerin.html', {'form': form})


def cam_view(request):
    posts = Campaign.objects.all().order_by('-date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    common_tags = Campaign.tags.most_common()[:]
    context = {
        'posts':posts,
        'common_tags':common_tags,
    }
    return render(request, 'Gngo/campaigns.html', context)


def cam_single(request, id):
    template_name = 'Gngo/campaigns-detail.html'
    cam = get_object_or_404(Campaign, id = id)
    
    cam_related = cam.tags.similar_objects()[:3]
    context = {
        'cam':cam,
        'cam_related':cam_related,
        'images': CampaignImages.objects.filter(post=cam),
    }
    context["object"] = Campaign.objects.get(id = id)
    return render(request, template_name, context)


def camtagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Campaign.tags.most_common()[:]
    posts = Campaign.objects.filter(tags=tag)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'Gngo/campaigns.html', context)

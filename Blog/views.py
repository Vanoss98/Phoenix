from django.shortcuts import render, redirect
from .models import MaghaalaatPost, AnjomanPost, SukhtegiPost, StoryPost
from .forms import BaseContactForm, HomeGholakForm, HomeContactForm
from django.contrib import messages
from django.views.generic import DetailView, ListView, TemplateView


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

class MainListView(TemplateView):
    template_name = 'Blog/Home.html'

    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        context['news'] = SukhtegiPost.objects.order_by('-published')[:2]
        context['posts'] = AnjomanPost.objects.order_by('-published')[:3]
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({'aform': HomeGholakForm(prefix='aform_pre'), 'bform': HomeContactForm(prefix='bform_pre')})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        aform = _get_form(request, HomeGholakForm, 'aform_pre')
        bform = _get_form(request, HomeContactForm, 'bform_pre')
        if aform.is_bound and aform.is_valid():
            aform.save()
            messages.success(request, f'اطلاعات با موفقیت ثبت شد')
            return redirect('Home-Page')
        elif bform.is_bound and bform.is_valid():
            bform.save()
            messages.success(request, f'اطلاعات با موفقیت ثبت شد')
            return redirect('Home-Page')
        context = self.get_context_data(**kwargs)
        context.update({'aform': aform, 'bform': bform})
        return self.render_to_response(context)


class Statistics(TemplateView):
    template_name = 'Blog/Statistics.html'


class Medics(TemplateView):
    template_name = 'Blog/Medic.html'


class Questions(TemplateView):
    template_name = 'Blog/Questions.html'


#----------------MAGHALAT-VIEWS----------------#

class MaghaleMain(ListView):
    model = MaghaalaatPost
    template_name = 'Blog/Blog-elmi.html'
    queryset = MaghaalaatPost.objects.all()
    context_object_name = 'posts'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(MaghaleMain, self).get_context_data(**kwargs)
        context['tags'] = MaghaalaatPost.tags.all()
        return context


class MaghaleTags(ListView):
    model = MaghaalaatPost
    template_name = 'Blog/Blog-elmi.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return MaghaalaatPost.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

    def get_context_data(self, **kwargs):
        context = super(MaghaleTags, self).get_context_data(**kwargs)
        context['tags'] = MaghaalaatPost.tags.all()
        return context


class MaghaleDetail(DetailView):
    model = MaghaalaatPost
    template_name = 'Blog/Blog-elmi-detail.html'
    context_object_name = 'maghaale'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_items"] = self.object.tags.similar_objects()[:3]
        context["images"] = self.object.maghaalaatimages_set.all()
        context["videos"] = self.object.maghaalaatvideos_set.all()
        return context

#----------------SUKHTEGI-VIEWS----------------#


class SukhtegiMain(ListView):
    model = SukhtegiPost
    template_name = 'Blog/Blog-snews.html'
    queryset = SukhtegiPost.objects.all()
    context_object_name = 'posts'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(SukhtegiMain, self).get_context_data(**kwargs)
        context['tags'] = SukhtegiPost.tags.all()
        return context


class SukhtegiTags(ListView):
    model = SukhtegiPost
    template_name = 'Blog/Blog-snews.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return SukhtegiPost.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

    def get_context_data(self, **kwargs):
        context = super(SukhtegiTags, self).get_context_data(**kwargs)
        context['tags'] = SukhtegiPost.tags.all()
        return context


class SukhtegiDetail(DetailView):
    model = SukhtegiPost
    template_name = 'Blog/Blog-snews-detail.html'
    context_object_name = 'khabar'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_items"] = self.object.tags.similar_objects()[:3]
        context["images"] = self.object.sukhtegiimages_set.all()
        context["videos"] = self.object.sukhtegivideos_set.all()
        return context

#----------------ANJOMAN-VIEWS----------------#


class AnjomanMain(ListView):
    model = AnjomanPost
    template_name = 'Blog/Blog-gnews.html'
    queryset = AnjomanPost.objects.all()
    context_object_name = 'posts'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(AnjomanMain, self).get_context_data(**kwargs)
        context['tags'] = AnjomanPost.tags.all()
        return context


class AnjomanTags(ListView):
    model = AnjomanPost
    template_name = 'Blog/Blog-gnews.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return AnjomanPost.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

    def get_context_data(self, **kwargs):
        context = super(AnjomanTags, self).get_context_data(**kwargs)
        context['tags'] = AnjomanPost.tags.all()
        return context


class AnjomanDetail(DetailView):
    model = AnjomanPost
    template_name = 'Blog/Blog-gnews-detail.html'
    context_object_name = 'khabar'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_items"] = self.object.tags.similar_objects()[:3]
        context["images"] = self.object.anjomanimages_set.all()
        context["videos"] = self.object.anjomanvideos_set.all()
        return context

#----------------STORY-VIEWS----------------#


class StoryMain(ListView):
    model = StoryPost
    template_name = 'Blog/Blog-stories.html'
    queryset = StoryPost.objects.all()
    context_object_name = 'posts'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(StoryMain, self).get_context_data(**kwargs)
        context['tags'] = StoryPost.tags.all()
        return context


class StoryTags(ListView):
    model = StoryPost
    template_name = 'Blog/Blog-stories.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return StoryPost.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

    def get_context_data(self, **kwargs):
        context = super(StoryTags, self).get_context_data(**kwargs)
        context['tags'] = StoryPost.tags.all()
        return context


class StoryDetail(DetailView):
    model = StoryPost
    template_name = 'Blog/Blog-stories-detail.html'
    context_object_name = 'khabar'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_items"] = self.object.tags.similar_objects()[:3]
        context["images"] = self.object.storyimages_set.all()
        context["videos"] = self.object.storyvideos_set.all()
        return context


def info(request):
    if request.method == 'POST':
        form = BaseContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'!اطلاعات با موفقیت ثبت شد')
    else:
        form = BaseContactForm()
    return redirect(request.META.get('HTTP_REFERER'))
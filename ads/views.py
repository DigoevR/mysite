from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from ads.owner import OwnerCreateView, OwnerDeleteView, OwnerDetailView, OwnerListView, OwnerUpdateView
from .models import Ad, Comment, Favorite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CreateForm, CommentForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

class AdsListView(OwnerListView):
    model = Ad
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorites = []
        if self.request.user.is_authenticated:
            favorites = self.request.user.favorite_ads.values_list('id', flat=True)
        context["favorites"] = favorites
        context["search"] = self.search
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.search = self.request.GET.get('search', False)
        if self.search:   
            queryset = queryset.filter(Q(title__contains=self.search) |
                                        Q(text__contains=self.search) |
                                        Q(tags__name__in=self.search.split(','))
                                        )
        return queryset


class AdsDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    def get(self, request, pk):
        ad = get_object_or_404(self.model.objects.prefetch_related('comment_set'), pk=pk)
        comments = ad.comment_set.all()
        form = CommentForm()
        context = {'ad': ad, 'comments': comments, 'comment_form': form}
        return render(request, self.template_name, context)


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class AdsCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')
    def get(self, request):
        form = CreateForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            form.save_m2m()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class AdsUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')
    def get(self, request, pk):
        ad = get_object_or_404(Ad.objects.filter(owner=request.user), pk=pk)
        form = CreateForm(instance=ad)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        ad = get_object_or_404(Ad.objects.filter(owner=request.user), pk=pk)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class AdsDeleteView(OwnerDeleteView):
    model = Ad
    success_url = reverse_lazy('ads:ad_list')


class CommentCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_detail.html'
    def post(self, request, pk):
        ad = get_object_or_404(Ad.objects.prefetch_related('comment_set'), pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data.get('comment'), ad=ad, owner=request.user)
            comment.save()
            return redirect(reverse_lazy('ads:ad_detail', args=[pk]))
        else:
            context = {'ad': ad, 'form': form, 'comments': ad.comment_set}
            return render(request, self.template_name, context)


class CommentDeleteView(OwnerDeleteView):
    model = Comment

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse_lazy('ads:ad_detail', args=[ad.id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        favorite, created = Favorite.objects.get_or_create(ad=ad, user=request.user)
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        Favorite.objects.filter(ad=ad, user=request.user).delete()
        return HttpResponse()

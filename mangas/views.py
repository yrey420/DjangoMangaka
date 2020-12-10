from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView

from .forms import MangaForms

# Create your views here.
from .models import Manga


@method_decorator(login_required, name="dispatch")
def revisar(request):
    return render(request, 'mangas/revisar.html')


@method_decorator(login_required, name="dispatch")
class MangaList(ListView):
    model = Manga


@method_decorator(login_required, name="dispatch")
class MangaDetail(DetailView):
    model = Manga


@method_decorator(login_required, name="dispatch")
class MangaCreate(SuccessMessageMixin, CreateView):
    model = Manga
    form_class = MangaForms
    template_name = 'mangas/manga_form.html'
    success_url = reverse_lazy('manga_list')
    success_message = "manga successfully created!"

    def post(self, request, *args):

        if request.method == "POST":
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                form.imageM = form.cleaned_data['portadaManga']
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


@method_decorator(login_required, name="dispatch")
class MangaUpdate(SuccessMessageMixin, UpdateView):
    model = Manga
    form_class = MangaForms
    success_url = reverse_lazy('manga_list')
    success_message = "Product successfully updated!"


@method_decorator(login_required, name="dispatch")
class MangaDelete(SuccessMessageMixin, DeleteView):
    model = Manga
    success_url = reverse_lazy('manga_list')
    success_message = "Product successfully deleted!"

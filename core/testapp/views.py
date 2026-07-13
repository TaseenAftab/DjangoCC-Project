from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from core.testapp.forms import CreateIFtaForm
from core.testapp.models import Ifta
from core.users.globals.mixins import HTMXFormMixin


class IftaListView(LoginRequiredMixin, ListView):
    model = Ifta
    template_name = "testapp/ifta_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Iftas List"
        context["form"] = CreateIFtaForm()
        return context


ifta_list_view = IftaListView.as_view()


class IftaDetailView(LoginRequiredMixin, DetailView):
    model = Ifta
    template_name = "testapp/partials/crud_partials.html#detail"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = f"{self.object.name}"
        return context


ifta_detail_view = IftaDetailView.as_view()


class IftaCreateView(HTMXFormMixin, LoginRequiredMixin, CreateView):
    model = Ifta
    form_class = CreateIFtaForm
    success_url = reverse_lazy("testapp:ifta_list")

    def get(self, request, *args, **kwargs):
        return redirect("testapp:ifta_list")

    def form_invalid(self, form):
        response = HttpResponse("Name or Fiqh is faulty.")
        response["HX-Retarget"] = "#create-ifta-error"
        return response


ifta_create_view = IftaCreateView.as_view()


class IftaUpdateView(
    LoginRequiredMixin,
    HTMXFormMixin,
    UpdateView,
):
    model = Ifta
    template_name = "testapp/partials/crud_partials.html#update"
    form_class = CreateIFtaForm
    slug_field = "name"
    slug_url_kwarg = "name"
    success_url = reverse_lazy("testapp:ifta_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Update Ifta"
        return context

    def form_invalid(self, form):
        response = HttpResponse("Name or Fiqh is faulty.")
        response["HX-Retarget"] = "#update-ifta-error"
        return response


ifta_update_view = IftaUpdateView.as_view()


class IftaDeleteView(
    LoginRequiredMixin,
    HTMXFormMixin,
    DeleteView,
):
    model = Ifta
    success_url = reverse_lazy("testapp:ifta_list")
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Delete Ifta"
        return context

    def get_success_url(self):
        return reverse_lazy("testapp:ifta_list")


ifta_delete_view = IftaDeleteView.as_view()

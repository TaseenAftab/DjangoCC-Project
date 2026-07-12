from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from core.testapp.forms import CreateIFtaForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from core.testapp.models import Ifta
from core.testapp.utils import add_toast




@login_required
def testview(request):

    return render(request, 'testapp/testview.html')

class IftaListView(LoginRequiredMixin, ListView):
    model = Ifta
    template_name = "testapp/ifta_list.html"

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Iftas List"
        context["form"] = CreateIFtaForm()
        return context

iftaView = IftaListView.as_view()

class IftaDetailView(LoginRequiredMixin, DetailView):
    model = Ifta
    template_name = "testapp/ifta_detail.html"
    slug_field='name'
    slug_url_kwarg='name'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = f"{self.object.name}"
        return context

ifta_detail_view = IftaDetailView.as_view()


class IftaCreateView(LoginRequiredMixin, CreateView):
    model = Ifta
    form_class = CreateIFtaForm
    success_url = reverse_lazy("testapp:ifta_list")  # <--- Add this line


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Add Ifta"
        return context
    
    def get(self, request, *args, **kwargs):
        return redirect("testapp:ifta_list")

ifta_create_view = IftaCreateView.as_view()


class IftaUpdateView(LoginRequiredMixin, UpdateView):
    model = Ifta
    template_name = "testapp/ifta_update.html"
    form_class = CreateIFtaForm
    slug_field='name'
    slug_url_kwarg='name'
    success_url = reverse_lazy("testapp:ifta_list")

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Update Ifta"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        response = add_toast(response, "Ifta updated successfully", "success")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        response = add_toast(response, "Ifta updated failed", "error")
        return response

ifta_update_view = IftaUpdateView.as_view()


class IftaDeleteView(LoginRequiredMixin, DeleteView):
    model = Ifta
    success_url = reverse_lazy("testapp:ifta_list")
    slug_field='name'
    slug_url_kwarg='name'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Delete Ifta"
        return context
    

ifta_delete_view = IftaDeleteView.as_view()
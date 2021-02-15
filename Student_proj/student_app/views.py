from django.shortcuts import render
from django.urls import reverse_lazy , reverse

from django.views.generic import (TemplateView,View,CreateView,UpdateView,
                                    ListView,DetailView,DeleteView)
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class StudentListView(ListView):
    context_object_name='student_list_view'
    model = models.Student_details
    template_name = "student_list.html"


class StudentDetailView(DetailView):
    context_object_name='student_detail_view'
    model = models.Student_details
    # template_name = "student_list.html"

class StudentCreateView(CreateView):
    context_object_name='add_details_view'
    model = models.Student_details
    fields=('name','age','message')
    template_name = "add_details.html"

class StudentUpdateView(UpdateView):
    context_object_name='update_details_view'
    model = models.Student_details
    fields=('name','age','message')
    template_name = "update_list.html"
    # success_url = reverse_lazy("student_app:student_list")


class StudentDeleteView(DeleteView):
    context_object_name = 'delete_details_view'
    model = models.Student_details
    template_name = "delete_list.html"
    success_url =  reverse_lazy("student_app:student_list")




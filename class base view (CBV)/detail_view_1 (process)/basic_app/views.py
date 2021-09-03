from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

# Create your views here. (Functional view)
#def index(request):
#    return render(request, 'index.html')

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
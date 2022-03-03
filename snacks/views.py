from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Snack

class HomePageView(TemplateView):
  template_name = 'base.html'
  
class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snack_list'


class SnackDetailsView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack
  context_object_name = 'snack_details'
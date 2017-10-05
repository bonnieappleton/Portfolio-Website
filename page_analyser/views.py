from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import PageAnalyserForm

class PageAnalyser(FormView):
    form_class = PageAnalyserForm
    template_name = 'url-form.html'
    success_url = 'analyser-report'
    
class AnalyserReport(TemplateView):
    template_name = 'analyser-report.html'

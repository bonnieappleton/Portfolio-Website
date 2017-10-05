from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import PageAnalyserForm

class PageAnalyser(FormView):
    form_class = PageAnalyserForm
    template_name = 'url-form.html'
    success_url = 'analyser-report'
    
    def form_valid(self, form):
        url = form.cleaned_data['url']
        PageAnalyserForm.analyse_page(url)
        return super(PageAnalyser, self).form_valid(form)


class AnalyserReport(TemplateView):
    template_name = 'analyser-report.html'

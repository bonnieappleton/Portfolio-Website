from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import ContactForm

class Homepage(TemplateView):
    template_name = 'home/homepage.html'
    
class Contact(FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = 'success'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(Contact, self).form_valid(form)

class ContactSuccess(TemplateView):
    template_name = 'home/contact-success.html'

from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView

from .forms import ContactForm

class Homepage(TemplateView):
    template_name = 'home/homepage.html'
    
class Contact(FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = 'success'

    def form_valid(self, form):
        subject = 'Website inquiry - ' + form.cleaned_data['name']
        message = form.cleaned_data['email_content']
        sender = form.cleaned_data['contact_email']
        recipients = ['bemappleton@gmail.com']

        send_mail(subject, message, sender, recipients)
        return super(Contact, self).form_valid(form)

class ContactSuccess(TemplateView):
    template_name = 'home/contact-success.html'

class JSProjects(TemplateView):
    template_name = 'js-projects/main.html'

class JSBooks(TemplateView):
    template_name = 'js-projects/books.html'
    
class JSRainbowCanvas(TemplateView):
    template_name = 'js-projects/rainbow-canvas.html'
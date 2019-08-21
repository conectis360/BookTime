from django.shortcuts import render
from main import forms
from django.views.generic.edit import FormView
from django.views.generic import TemplateView



class ContactUsView(FormView):
    template_name = 'contact_form.html'
    form_class = forms.ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = 'home.html'
    

class AboutPageView(TemplateView):
    template_name = 'about_us.html'

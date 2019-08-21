#pages/urls.py

from django.urls import path
from . import views
from main import views


urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home'
        ),
    
    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name = 'contact_us',
    ),
    
    path(
        'about-us/',
        views.AboutPageView.as_view(),
        name='about_us'
        ),
    
    
]

#pages/urls.py

from django.urls import path
from . import views
from main import views
from django.views.generic.detail import DetailView
from main import models


urlpatterns = [
    
    path(
        "product/<slug:slug>/",
        DetailView.as_view(model=models.Product),
        name="product",
    ),
    
    path(
        "products/<slug:tag>/",
        views.ProductListView.as_view(),
        name="products",
        ),

    path(
        '',
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

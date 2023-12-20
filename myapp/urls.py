from django.urls import path
from .views import form_success_view, home_view, participant_form_view



urlpatterns = [
    path('home', home_view, name='home'),
    path('', participant_form_view, name='participant_form'),
    path('form_success/', form_success_view, name='form_success'),
    
   
]

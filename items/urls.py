from django.urls import path
from .views import submit_complaint

urlpatterns = [
    path('submit-complaint/', submit_complaint, name='submit_complaint'),
]

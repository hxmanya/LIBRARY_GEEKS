from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('for_kids/', views.for_kids, name='for_kids'),
    path('for_teenagers/', views.for_teenagers, name='for_teenagers'),
    path('for_youths/', views.for_youths, name='for_youths'),
    path('for_pensioners/', views.for_pensioners, name='for_pensioners'),
]
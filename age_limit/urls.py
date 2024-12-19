from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('for_kids/', views.ForKidsView.as_view(), name='for_kids'),
    path('for_teenagers/', views.ForTeenagersView.as_view(), name='for_teenagers'),
    path('for_youths/', views.ForYouthsView.as_view(), name='for_youths'),
    path('for_pensioners/', views.ForPensionersView.as_view(), name='for_pensioners'),
]
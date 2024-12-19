from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('about_pets/', views.AboutPetsView.as_view(), name='about_pets'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]
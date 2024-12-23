from django.urls import path
from . import views

urlpatterns = [
    path('mybook_list/', views.MyBookView.as_view(), name='mybook_list'),
    path('form_parser_mybook/', views.MyBookFormView.as_view()),
]
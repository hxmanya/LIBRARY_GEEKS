from django.urls import path
from . import views
urlpatterns = [
    path('basket/', views.basket_list_view, name='basket_list'),
    path('basket/create/', views.create_basket_view, name='create_basket'),
    path('basket/<int:id>/', views.basket_detail_view, name='basket_detail'),
    path('basket/<int:id>/edit/', views.update_basket_view, name='update_basket'),
    path('basket/<int:id>/delete/', views.delete_basket_view, name='delete_basket'),
]
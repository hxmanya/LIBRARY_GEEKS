from django.urls import path
from . import views
urlpatterns = [
    path('basket/', views.BasketListView.as_view(), name='basket_list'),
    path('basket/create/', views.CreateBasketView.as_view(), name='create_basket'),
    path('basket/<int:id>/', views.BasketDetailView.as_view(), name='basket_detail'),
    path('basket/<int:id>/edit/', views.UpdateBasketView.as_view(), name='update_basket'),
    path('basket/<int:id>/delete/', views.DeleteBasketView.as_view(), name='delete_basket'),
]
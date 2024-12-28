from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<int:recipe_id>/ingredient/add/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredient/<int:pk>/edit/', views.IngredientUpdateView.as_view(), name='ingredient_edit'),
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('collection/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('collection/create/', views.CollectionCreateView.as_view(), name='collection_create'),
    path('search_recipe/', views.SearchView.as_view(), name='search_recipe'),
]
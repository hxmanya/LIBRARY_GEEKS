from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.messages.views import SuccessMessageMixin
from .models import Recipe, Ingredient, Collection
from .forms import RecipeForm, IngredientForm, CollectionForm


class SearchView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=recipe_id)


class RecipeCreateView(SuccessMessageMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')
    success_message = "Рецепт успешно создан"


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')

    # Перенаправляем сразу без подтверждения
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'id': self.kwargs['recipe_id']})


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'id': self.object.recipe.id})


class CollectionListView(ListView):
    model = Collection
    template_name = 'recipes/collection_list.html'
    context_object_name = 'collections'


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'recipes/collection_detail.html'
    context_object_name = 'collection'


class CollectionCreateView(SuccessMessageMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'recipes/collection_form.html'
    success_url = reverse_lazy('collection_list')
    success_message = "Коллекция успешно создана"

# Create your views here.

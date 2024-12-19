from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm
from django.views import generic


class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)

# def create_basket_view(request):
#     if request.method == 'POST':
#         form = BasketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = BasketForm()
#     return render(request, 'basket/create_basket.html', context={'form': form})

class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = Basket

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



# def basket_list_view(request):
#     if request.method == 'GET':
#         basket_list = Basket.objects.all().order_by('-id')
#         context = {'basket_list': basket_list}
#         return render(request, 'basket/basket_list.html', context=context)

class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)



# def basket_detail_view(request, id):
#     if request.method == 'GET':
#         basket = get_object_or_404(Basket, id=id)
#         context = {'basket': basket}
#         return render(request, 'basket/basket_detail.html', context=context)


class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/update_basket.html'
    form_class = BasketForm
    success_url = '/basket/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)



# def update_basket_view(request, id):
#     basket = get_object_or_404(Basket, id=id)
#     if request.method == 'POST':
#         form = BasketForm(request.POST, instance=basket)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = BasketForm(instance=basket)
#     return render(request, 'basket/update_basket.html', context={'form': form, 'basket': basket})


class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/delete_basket.html'
    success_url = '/basket/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)

# def delete_basket_view(request, id):
#     basket = get_object_or_404(Basket, id=id)
#     if request.method == 'POST':
#         basket.delete()
#         return redirect('basket_list')
#     return render(request, 'basket/delete_basket.html', context={'basket': basket})
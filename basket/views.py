from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm


def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm()
    return render(request, 'basket/create_basket.html', context={'form': form})

def basket_list_view(request):
    if request.method == 'GET':
        basket_list = Basket.objects.all().order_by('-id')
        context = {'basket_list': basket_list}
        return render(request, 'basket/basket_list.html', context=context)

def basket_detail_view(request, id):
    if request.method == 'GET':
        basket = get_object_or_404(Basket, id=id)
        context = {'basket': basket}
        return render(request, 'basket/basket_detail.html', context=context)

def update_basket_view(request, id):
    basket = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=basket)
    return render(request, 'basket/update_basket.html', context={'form': form, 'basket': basket})

def delete_basket_view(request, id):
    basket = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        basket.delete()
        return redirect('basket_list')
    return render(request, 'basket/delete_basket.html', context={'basket': basket})
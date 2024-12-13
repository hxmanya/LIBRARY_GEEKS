from django.shortcuts import render

from . import models


def all_books(request):
    if request.method == 'GET':
        books = models.Book.objects.all().order_by('-id')
        context = {'books': books}
        return render(request,
                      template_name='tags/all_books.html',
                      context=context
                      )

def for_kids(request):
    if request.method == 'GET':
        books_kid = models.Book.objects.filter(tags__name='для детей').order_by('-id')
        context = {'books_kid': books_kid}
        return render(request,
                      template_name='tags/for_kids.html',
                      context=context
                      )

def for_teenagers(request):
    if request.method == 'GET':
        books_teenager = models.Book.objects.filter(tags__name='для подростков').order_by('-id')
        context = {'books_teenager': books_teenager}
        return render(request,
                      template_name='tags/for_teenagers.html',
                      context=context
                      )


def for_youths(request):
    if request.method == 'GET':
        books_youth = models.Book.objects.filter(tags__name='для молодежи').order_by('-id')
        context = {'books_youth': books_youth}
        return render(request,
                      template_name='tags/for_youths.html',
                      context=context
                      )

def for_pensioners(request):
    if request.method == 'GET':
        books_pensioner = models.Book.objects.filter(tags__name='для пенсионеров').order_by('-id')
        context = {'books_pensioner': books_pensioner}
        return render(request,
                      template_name='tags/for_pensioners.html',
                      context=context
                      )

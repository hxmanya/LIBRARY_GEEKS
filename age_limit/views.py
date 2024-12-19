from django.shortcuts import render
from django.views import generic
from . import models


class AllBooksView(generic.ListView):
    template_name = 'tags/all_books.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('id')




# def all_books(request):
#     if request.method == 'GET':
#         books = models.Book.objects.all().order_by('-id')
#         context = {'books': books}
#         return render(request,
#                       template_name='tags/all_books.html',
#                       context=context
#                       )

class ForKidsView(generic.ListView):
    template_name = 'tags/for_kids.html'
    context_object_name = 'books_kid'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='для детей').order_by('-id')

# def for_kids(request):
#     if request.method == 'GET':
#         books_kid = models.Book.objects.filter(tags__name='для детей').order_by('-id')
#         context = {'books_kid': books_kid}
#         return render(request,
#                       template_name='tags/for_kids.html',
#                       context=context
#                       )

class ForTeenagersView(generic.ListView):
    template_name = 'tags/for_teenagers.html'
    context_object_name = 'books_teenager'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='для подростков').order_by('-id')

# def for_teenagers(request):
#     if request.method == 'GET':
#         books_teenager = models.Book.objects.filter(tags__name='для подростков').order_by('-id')
#         context = {'books_teenager': books_teenager}
#         return render(request,
#                       template_name='tags/for_teenagers.html',
#                       context=context
#                       )
#

class ForYouthsView(generic.ListView):
    template_name = 'tags/for_youths.html'
    context_object_name = 'books_youth'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='для молодежи').order_by('-id')


# def for_youths(request):
#     if request.method == 'GET':
#         books_youth = models.Book.objects.filter(tags__name='для молодежи').order_by('-id')
#         context = {'books_youth': books_youth}
#         return render(request,
#                       template_name='tags/for_youths.html',
#                       context=context
#                       )


class ForPensionersView(generic.ListView):
    template_name = 'tags/for_pensioners.html'
    context_object_name = 'books_pensioner'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='для пенсионеров').order_by('-id')

# def for_pensioners(request):
#     if request.method == 'GET':
#         books_pensioner = models.Book.objects.filter(tags__name='для пенсионеров').order_by('-id')
#         context = {'books_pensioner': books_pensioner}
#         return render(request,
#                       template_name='tags/for_pensioners.html',
#                       context=context
#                       )

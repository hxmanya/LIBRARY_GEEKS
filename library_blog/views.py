from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.views import generic
from django.urls import reverse

from . import models
from .models import BookModel
from .forms import ReviewForm


class BookListView(generic.ListView):
    model = BookModel
    template_name = "book.html"
    context_object_name = "book_list"

    def get_queryset(self):
        return BookModel.objects.all().order_by('-id')

class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"
    context_object_name = "book_detail"

    def get_object(self, **kwargs):
        return get_object_or_404(BookModel, id=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm()
        context["reviews"] = self.object.reviews.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.save()
            return redirect(reverse("book_detail", kwargs={"id": self.object.id}))
        else:
            context = self.get_context_data()
            context["review_form"] = form
            return self.render_to_response(context)

# def book_list_view(request):
#     if request.method == 'GET':
#         book_list = models.BookModel.objects.all().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request, 'book.html', context=context)



def book_detail_view(request, id):
    book = get_object_or_404(BookModel, id=id)
    reviews = book.reviews.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect("book_detail", id=book.id)
    else:
        form = ReviewForm()
    context = {
        "book_id": book,
        "review_form": form,
        "reviews": reviews,
    }
    return render(request, "book_detail.html", context)

# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse("Меня зовут Аман. 19 лет. Студент GEEKS.")
#
# def about_pets(request):
#     if request.method == 'GET':
#         return HttpResponse("Кот. Зовут Рыжик. 1 год. Не женат.")
#
# def system_time(request):
#     if request.method == 'GET':
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         return HttpResponse(f"Текущее системное время: {current_time}")


class AboutMeView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Меня зовут Аман. 19 лет. Студент GEEKS.")

# Описание питомца
class AboutPetsView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Кот. Зовут Рыжик. 1 год. Не женат.")

# Текущее время
class SystemTimeView(generic.View):
    def get(self, request, *args, **kwargs):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее системное время: {current_time}")
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from . import models
from .models import BookModel
from .forms import ReviewForm


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {'book_id': book_id}
        return render(request, 'book_detail.html', context=context)



def book_list_view(request):
    if request.method == 'GET':
        book_list = models.BookModel.objects.all().order_by('-id')
        context = {'book_list': book_list}
        return render(request, 'book.html', context=context)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Аман. 19 лет. Студент GEEKS.")

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse("Кот. Зовут Рыжик. 1 год. Не женат.")

def system_time(request):
    if request.method == 'GET':
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее системное время: {current_time}")

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


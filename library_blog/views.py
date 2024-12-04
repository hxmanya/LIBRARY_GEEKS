from django.shortcuts import render
from django.http import HttpResponse
import datetime


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


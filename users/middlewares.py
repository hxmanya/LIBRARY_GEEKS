from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class LvlMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            lvl = str(request.POST.get('lvl'))
            if lvl == 'Ниже Junior':
                return HttpResponseBadRequest('Пожалуста подтяните ваш уровень')
            elif lvl == 'Junior':
                request.salary = '700$'
            elif lvl == 'Middle':
                request.salary = '1000$'
            elif lvl == 'Senior':
                request.salary = '2000$'
            else:
                return HttpResponseBadRequest('Ваш уровень нам не понятен, вы не подходите')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Не определена зп')




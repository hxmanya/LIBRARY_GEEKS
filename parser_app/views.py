from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import generic

class MyBookView(generic.ListView):
    template_name = 'parser/mybook_list.html'
    context_object_name = 'mybook'
    model = models.MyBook
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class MyBookFormView(generic.FormView):
    template_name = 'parser/mybook_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(MyBookFormView, self).post(request, *args, **kwargs)





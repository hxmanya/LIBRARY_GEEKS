from django import forms
from . import models, parser_mybook

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('my_book', 'my_book'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'my_book':
            mybook_file = parser_mybook.parsing()
            for i in mybook_file:
                models.MyBook.objects.create(**i)

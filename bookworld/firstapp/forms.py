from django import forms
from .models import Person, Image

# class UserForm(forms.Form):
#     name = forms.CharField(label='Имя клиента', help_text='need to write your name', label_suffix='---->>>',
#                            initial='Введите ФИО')
#     age = forms.IntegerField(label='Возраст клиента')
#     field_order = ['age', 'name'] - позволяет менять порядок следования полей формы

class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
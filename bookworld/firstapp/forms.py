from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(label='Имя клиента', help_text='need to write your name', label_suffix='---->>>',
#                            initial='Введите ФИО')
#     age = forms.IntegerField(label='Возраст клиента')
#     field_order = ['age', 'name'] - позволяет менять порядок следования полей формы

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента",
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента",
                             widget=forms.NumberInput(attrs={"class": "myfield"}))
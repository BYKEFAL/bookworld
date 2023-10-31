from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(label='Имя клиента', help_text='need to write your name', label_suffix='---->>>',
#                            initial='Введите ФИО')
#     age = forms.IntegerField(label='Возраст клиента')
#     field_order = ['age', 'name'] - позволяет менять порядок следования полей формы

class UserForm(forms.Form):
    name = forms.CharField(label='Имя') 
    age = forms.IntegerField(label='Возраст клиента')
    comment = forms.CharField(label='Коментарий', widget=forms.Textarea) 
from .forms import UserForm, ImageForm
from django.shortcuts import render, redirect
from .models import Person, Image
from django.http import HttpResponseNotFound


def index(request):
    my_text = 'Изучаем модели Django'
    people_kol = Person.objects.count()
    context = {'my_text': my_text, "people_kol": people_kol}
    return render(request, "firstapp/index.html", context)


def about(request):
    return render(request, "firstapp/about.html")


def contact(request):
    return render(request, "firstapp/contact.html")


# взаимодействие с формой ввода данных о клиентах
def my_form(request):
    if request.method == "POST":  # пользователь отправил данные
        form = UserForm(request.POST)  # создание экземпляра формы
        if form.is_valid():  # проверка валидности формы
            form.save()  # запись данных в БД
            # остаемся на той же странице, обновляем форму

    # Загрузить форму для ввода клиентов
    my_text = 'Сведения о клиентах'
    people = Person.objects.all()
    form = UserForm()
    context = {'my_text': my_text, "people": people, "form": form}
    return render(request, "firstapp/my_form.html", context)

# изменение данных о клиенте в БД
def edit_form(request, id):
    person = Person.objects.get(id=id)
    # Если пользователь вернул отредактированные данные
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('my_form')

    # Если пользователь отправляет данные на редактирование
    data = {"person": person}
    return render(request, "firstapp/edit_form.html", context=data)


# удаление данных о клиенте из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
    
# загрузка изображений
def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные изображения'
    my_img = Image.objects.all()
    form = ImageForm()
    context = {'my_text': my_text, "my_img": my_img, "form": form}
    return render(request, 'firstapp/form_up_img.html', context)


# удаление изображения из БД
def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
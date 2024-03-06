from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # object_person = models.Manager() #(переименовали  objects, в object_person)
    DoesNotExist = models.Manager


class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    
class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

# Загрузка изображений
class Image(models.Model):
    title = models.CharField(max_length=100, null=False,
                             verbose_name="Описание изображения",)
    image = models.ImageField(upload_to='images',
                              verbose_name="Файл с изображением",
                              null=True, blank=True)
    # obj_img = models.Manager()

    def __str__(self):
        return self.title




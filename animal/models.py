from django.db import models
from django.utils import timezone
from django.core import validators
from django.urls import reverse
# import uuid

KIND_ANIMAL = [('1', 'CAT')
            , ('2', 'PARROT')
            , ('3', 'DOG'),]

# справочник пород животных
class Breed(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, verbose_name="Порода")
    code = models.CharField(max_length=256, verbose_name="Код")

    def __str__(self):
        return self.name

# Create your models here.
class Animal(models.Model):
    """Main animal description"""

    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT,verbose_name="Порода")
    age = models.IntegerField(verbose_name="Возраст", validators=[validators.MaxValueValidator(100)])
    describe = models.TextField(blank=True, verbose_name="Описание")
    d_receipt = models.DateTimeField(verbose_name="Дата поступления")
    kind = models.CharField(max_length=3, choices = KIND_ANIMAL, verbose_name="Вид животного")
    photo = models.ImageField(upload_to='anim_photo' , blank=True, verbose_name="Фото")
    vaccinated = models.BooleanField(default=False, verbose_name="Привит")

    def __str__(self):
        return '{} {}'.format(self.name, self.breed)
    # вызывается для получения адреса страницы для редиректа
    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={ 'pk': self.pk })
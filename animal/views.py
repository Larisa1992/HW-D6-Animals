from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView

from animal.models import Animal, Breed

# домашняя страница
class HomePageView(TemplateView):

    template_name = "home.html"
    # словарь параметров для шаблона (метод get_context_data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_us"] = 'Мы любим животных и хотим, чтобы у каждого питомца был свой заботливый хозяин'
        context["img_url"] = 'img/animal.svg'
        return context

# страница животного (DetailView)
# animal_detail.html - по умолчанию ищет шаблон с таким названием
# Ссылка на нужный объект object генерируется под капотом класса DetailView
# в шаблоне животному обращаться по имени object
class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'

#список всех животных (ListView)
# по умолчанию выводит шаблон под названием animal_list.html
class AnimalListView(ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = "all_animals" #если этот атрибут не указан, то внутри шаблона данные будут доступны по имени object_list

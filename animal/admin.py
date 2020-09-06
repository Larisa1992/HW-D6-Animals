from django.contrib import admin
from animal.models import Animal, Breed

# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_filter = ('kind',)

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

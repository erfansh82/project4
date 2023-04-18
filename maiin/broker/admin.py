from django.contrib import admin
from .models import Information,State,Field


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=('name','prof_image',)
    search_fields=('name','prof_image',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display=('title','description',)
    search_fields=('title','description',)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display=('s_information','field',)
    search_fields=('s_information','field',)
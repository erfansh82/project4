from django.contrib import admin
from .models import CreatePlan,ActivePlan

@admin.register(CreatePlan)
class CreatePlanAdmin(admin.ModelAdmin):
    list_display=('title','days','country','price',)
    search_fields=('title','days','country','price',)


@admin.register(ActivePlan)
class ActivePlanAdmin(admin.ModelAdmin):
    list_display=('username','choose_plan',)
    search_fields=('username','choose_plan',)


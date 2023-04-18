from django.contrib import admin
from .models import User ,UserProfile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username',)
    search_fields=('username',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','gender','birth_date','country','wallet_number','wallet',)
    search_fields=('user','gender','country',)
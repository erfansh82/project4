from django.contrib import admin
from .models import VerifyAccount,VerifyAccount2


@admin.register(VerifyAccount)
class VerifyAdmin(admin.ModelAdmin):
    list_display=('user','pasport_image_front','pasport_image_back','verify_link',)
    search_fields=('user','verify_link',)


@admin.register(VerifyAccount2)
class VerifyAdmin2(admin.ModelAdmin):
    list_display=('user','broker_name','referral_code','referral_link','account_balance','account_number','gmail',)
    search_fields=('user','broker_name','referral_code','gmail','account_number',)



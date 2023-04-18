from django.contrib import admin
from .models import Explore,ExplorVerify


@admin.register(Explore)
class ExploreAdmin(admin.ModelAdmin):
    list_display=('forex_signal','crypto_signal',)
    search_fields=('forex_signal','crypto_signal',)


@admin.register(ExplorVerify)
class ExploreVerifyAdmin(admin.ModelAdmin):
    list_display=('forex_signal','crypto_signal',)
    search_fields=('forex_signal','crypto_signal',)
from django.contrib import admin

from .models import ForexSignal,CryptoSignal,ForexSignal2,CryptoSignal2

@admin.register(ForexSignal)
class ForexSignalAdmin(admin.ModelAdmin):
    list_display=('user','market_watch','live_price','signal_type','entry_price','take_profit','stop_loss','forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)


@admin.register(CryptoSignal)
class CryptoSignalAdmin(admin.ModelAdmin):
    list_display=('user','market_watch','live_price','signal_type','entry_price','take_profit','stop_loss','crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)



@admin.register(ForexSignal2)
class ForexSignal2Admin(admin.ModelAdmin):
    list_display=('verify','market_watch','live_price','signal_type','entry_price','take_profit','stop_loss','forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)



@admin.register(CryptoSignal2)
class CryptoSignal2Admin(admin.ModelAdmin):
    list_display=('verify','market_watch','live_price','signal_type','entry_price','take_profit','stop_loss','crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)

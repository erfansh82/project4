from django.db import models


class ForexSignal(models.Model):
    SIGNAL_CHOICE=(
        ("sell","sell"),
        ("buy","buy"),
        ("sell limit","sell limit"),
        ("sell stop","sell stop"),
        ("buy limit","buy limit"),
        ("buy stop","buy stop"),
    )
    MARKET_WATCH=(
        ("EURUSD","EURUSD"),
        ("EURCHF","EURCHF"),
        ("EURGBP","EURGBP"),
        ("EURJPY","EURJPY"),
        ("EURAUD","EURAUD"),
        ("EURNZD","EURNZD"),
        ("EURCAD","EURCAD"),
        ("USDJPY","USDJPY"),
        ("USDCAD","USDCAD"),
        ("USDCHF","USDCHF"),
        ("CADCHF","CADCHF"),
        ("CADJPY","CADJPY"),
        ("CHFJPY","CHFJPY"),
        ("GBPJPY","GBPJPY"),
        ("GBPCHF","GBPCHF"),
        ("GBPUSD","GBPUSD"),
        ("GBPNZD","GBPNZD"),
        ("GBPAUD","GBPAUD"),
        ("GBPCAD","GBPCAD"),
        ("AUDUSD","AUDUSD"),
        ("AUDCAD","AUDCAD"),
        ("AUDCHF","AUDCHF"),
        ("AUDJPY","AUDJPY"),
        ("AUDNZD","AUDNZD"),
        ("NZDUSD","NZDUSD"),
        ("NZDCAD","NZDCAD"),
        ("NZDCHF","NZDCHF"),
        ("NZDJPY","NZDJPY"),
        ("XAUUSD","XAUUSD"),
    )
    user=models.ForeignKey("register.UserProfile",on_delete=models.CASCADE)
    market_watch=models.CharField(max_length=20,choices=MARKET_WATCH)
    live_price=models.DecimalField(max_digits=5,decimal_places=2)
    signal_type=models.CharField(max_length=25,choices=SIGNAL_CHOICE)
    entry_price=models.IntegerField(default=0,null=True,blank=True)
    take_profit=models.IntegerField(default=0,null=True,blank=True)
    stop_loss=models.IntegerField(default=0,null=True,blank=True)
    forex_winrate=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss_pips=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit_pips=models.IntegerField(default=0,null=True,blank=True)
    total_signal=models.IntegerField(default=0,null=True,blank=True)
 
    def __str__(self):
        return f'{self.user}'


class CryptoSignal(models.Model):
    SIGNAL_CHOICE=(
        ("sell","sell"),
        ("buy","buy"),
        ("sell limit","sell limit"),
        ("sell stop","sell stop"),
        ("buy limit","buy limit"),
        ("buy stop","buy stop"),
    )
    MARKET_WATCH=(
        ("EURUSD","EURUSD"),
        ("EURCHF","EURCHF"),
        ("EURGBP","EURGBP"),
        ("EURJPY","EURJPY"),
        ("EURAUD","EURAUD"),
        ("EURNZD","EURNZD"),
        ("EURCAD","EURCAD"),
        ("USDJPY","USDJPY"),
        ("USDCAD","USDCAD"),
        ("USDCHF","USDCHF"),
        ("CADCHF","CADCHF"),
        ("CADJPY","CADJPY"),
        ("CHFJPY","CHFJPY"),
        ("GBPJPY","GBPJPY"),
        ("GBPCHF","GBPCHF"),
        ("GBPUSD","GBPUSD"),
        ("GBPNZD","GBPNZD"),
        ("GBPAUD","GBPAUD"),
        ("GBPCAD","GBPCAD"),
        ("AUDUSD","AUDUSD"),
        ("AUDCAD","AUDCAD"),
        ("AUDCHF","AUDCHF"),
        ("AUDJPY","AUDJPY"),
        ("AUDNZD","AUDNZD"),
        ("NZDUSD","NZDUSD"),
        ("NZDCAD","NZDCAD"),
        ("NZDCHF","NZDCHF"),
        ("NZDJPY","NZDJPY"),
        ("XAUUSD","XAUUSD"),
    )
    user=models.ForeignKey("register.UserProfile",on_delete=models.CASCADE)
    market_watch=models.CharField(max_length=20,choices=MARKET_WATCH)
    live_price=models.DecimalField(max_digits=5,decimal_places=2)
    signal_type=models.CharField(max_length=25,choices=SIGNAL_CHOICE)
    entry_price=models.IntegerField(default=0,null=True,blank=True)
    take_profit=models.IntegerField(default=0,null=True,blank=True)
    stop_loss=models.IntegerField(default=0,null=True,blank=True)
    crypto_winrate=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss_pips=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit_pips=models.IntegerField(default=0,null=True,blank=True)
    total_signal=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{self.user}'
    


class ForexSignal2(models.Model):
    SIGNAL_CHOICE=(
        ("sell","sell"),
        ("buy","buy"),
        ("sell limit","sell limit"),
        ("sell stop","sell stop"),
        ("buy limit","buy limit"),
        ("buy stop","buy stop"),
    )
    MARKET_WATCH=(
        ("EURUSD","EURUSD"),
        ("EURCHF","EURCHF"),
        ("EURGBP","EURGBP"),
        ("EURJPY","EURJPY"),
        ("EURAUD","EURAUD"),
        ("EURNZD","EURNZD"),
        ("EURCAD","EURCAD"),
        ("USDJPY","USDJPY"),
        ("USDCAD","USDCAD"),
        ("USDCHF","USDCHF"),
        ("CADCHF","CADCHF"),
        ("CADJPY","CADJPY"),
        ("CHFJPY","CHFJPY"),
        ("GBPJPY","GBPJPY"),
        ("GBPCHF","GBPCHF"),
        ("GBPUSD","GBPUSD"),
        ("GBPNZD","GBPNZD"),
        ("GBPAUD","GBPAUD"),
        ("GBPCAD","GBPCAD"),
        ("AUDUSD","AUDUSD"),
        ("AUDCAD","AUDCAD"),
        ("AUDCHF","AUDCHF"),
        ("AUDJPY","AUDJPY"),
        ("AUDNZD","AUDNZD"),
        ("NZDUSD","NZDUSD"),
        ("NZDCAD","NZDCAD"),
        ("NZDCHF","NZDCHF"),
        ("NZDJPY","NZDJPY"),
        ("XAUUSD","XAUUSD"),
    )
    verify=models.ForeignKey('verification.VerifyAccount',on_delete=models.CASCADE)
    market_watch=models.CharField(max_length=20,choices=MARKET_WATCH)
    live_price=models.DecimalField(max_digits=5,decimal_places=2)
    signal_type=models.CharField(max_length=25,choices=SIGNAL_CHOICE)
    entry_price=models.IntegerField(default=0,null=True,blank=True)
    take_profit=models.IntegerField(default=0,null=True,blank=True)
    stop_loss=models.IntegerField(default=0,null=True,blank=True)
    forex_winrate=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss_pips=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit_pips=models.IntegerField(default=0,null=True,blank=True)
    total_signal=models.IntegerField(default=0,null=True,blank=True)
 

    def __str__(self):
        return f'{self.verify}'
    

class CryptoSignal2(models.Model):
    SIGNAL_CHOICE=(
        ("sell","sell"),
        ("buy","buy"),
        ("sell limit","sell limit"),
        ("sell stop","sell stop"),
        ("buy limit","buy limit"),
        ("buy stop","buy stop"),
    )
    MARKET_WATCH=(
        ("EURUSD","EURUSD"),
        ("EURCHF","EURCHF"),
        ("EURGBP","EURGBP"),
        ("EURJPY","EURJPY"),
        ("EURAUD","EURAUD"),
        ("EURNZD","EURNZD"),
        ("EURCAD","EURCAD"),
        ("USDJPY","USDJPY"),
        ("USDCAD","USDCAD"),
        ("USDCHF","USDCHF"),
        ("CADCHF","CADCHF"),
        ("CADJPY","CADJPY"),
        ("CHFJPY","CHFJPY"),
        ("GBPJPY","GBPJPY"),
        ("GBPCHF","GBPCHF"),
        ("GBPUSD","GBPUSD"),
        ("GBPNZD","GBPNZD"),
        ("GBPAUD","GBPAUD"),
        ("GBPCAD","GBPCAD"),
        ("AUDUSD","AUDUSD"),
        ("AUDCAD","AUDCAD"),
        ("AUDCHF","AUDCHF"),
        ("AUDJPY","AUDJPY"),
        ("AUDNZD","AUDNZD"),
        ("NZDUSD","NZDUSD"),
        ("NZDCAD","NZDCAD"),
        ("NZDCHF","NZDCHF"),
        ("NZDJPY","NZDJPY"),
        ("XAUUSD","XAUUSD"),
    )
    verify=models.ForeignKey('verification.VerifyAccount',on_delete=models.CASCADE)
    market_watch=models.CharField(max_length=20,choices=MARKET_WATCH)
    live_price=models.DecimalField(max_digits=5,decimal_places=2)
    signal_type=models.CharField(max_length=25,choices=SIGNAL_CHOICE)
    entry_price=models.IntegerField(default=0,null=True,blank=True)
    take_profit=models.IntegerField(default=0,null=True,blank=True)
    stop_loss=models.IntegerField(default=0,null=True,blank=True)
    crypto_winrate=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit=models.IntegerField(default=0,null=True,blank=True)
    total_stop_loss_pips=models.IntegerField(default=0,null=True,blank=True)
    total_take_profit_pips=models.IntegerField(default=0,null=True,blank=True)
    total_signal=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{self.verify}'



    

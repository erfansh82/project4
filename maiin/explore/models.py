from django.db import models

class Explore(models.Model):
    forex_signal=models.ForeignKey('createsignal.ForexSignal',on_delete=models.CASCADE)
    crypto_signal=models.ForeignKey('createsignal.CryptoSignal',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.forex_signal}-{self.crypto_signal}'


class ExplorVerify(models.Model):
    forex_signal=models.ForeignKey('createsignal.ForexSignal2',on_delete=models.CASCADE)
    crypto_signal=models.ForeignKey('createsignal.CryptoSignal2',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.forex_signal}-{self.crypto_signal}'



from django.db import models
from register.models import User

class CreatePlan(models.Model):
    STATUS_CHOICE=(
        ('show','show'),
        ('hide','hide'),
    )
    title=models.CharField(max_length=100)
    days=models.IntegerField(default=0)
    minimum_winrate=models.IntegerField(default=0)
    maximum_winrate=models.IntegerField(default=0)
    country=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    forex_signal_limit=models.IntegerField(default=0)
    crypto_signal_limit=models.IntegerField(default=0)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='show')

    def __str__(self):
        return f'{self.title}'
    

class ActivePlan(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    choose_plan=models.ForeignKey(CreatePlan,on_delete=models.CASCADE)
    broker_referral=models.TextField()

    def __str__(self):
        return f'{self.username}-{self.choose_plan}'

    


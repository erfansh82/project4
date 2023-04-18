from django.db import models

class VerifyAccount(models.Model):
    user=models.OneToOneField('register.User',on_delete=models.CASCADE)
    pasport_image_front=models.ImageField(upload_to='image/')
    pasport_image_back=models.ImageField(upload_to='image/')
    verify_link=models.CharField(max_length=256)

    def __str__(self):
        return f'{self.user}'
    

class VerifyAccount2(models.Model):
    user=models.OneToOneField('register.User',on_delete=models.CASCADE)
    broker_name=models.CharField(max_length=256)
    referral_code=models.CharField(max_length=50)
    referral_link=models.CharField(max_length=256)
    description=models.TextField()
    account_balance=models.IntegerField(default=0)
    account_number=models.CharField(max_length=20)
    gmail=models.EmailField()

    def __str__(self):
        return f'{self.user}'

    




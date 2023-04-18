from django.db import models

class State(models.Model):
    name=models.CharField(max_length=50)
    prof_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.name} -- {self.prof_image}'
    

class Field(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return f'{self.title} = {self.description}'


class Information(models.Model):
    s_information=models.ForeignKey(State,related_name='sinfo',on_delete=models.CASCADE)
    field=models.ForeignKey(Field,related_name='fields',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.s_information} - {self.field}'

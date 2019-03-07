from django.db import models
class place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    def __str__(self):
        return "The restaurant"+self.name

class Restaurant(models.Model):
    place=models.OneToOneField(place,on_delete=models.CASCADE ,primary_key=True,)
    server_not_dogs=models.BooleanField(default=False)
    server_pizza=models.BooleanField(default=False)
    def __str__(self):
        return "The restaurant"+self.place.name

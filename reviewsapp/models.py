from tkinter import CASCADE
from django.db import models
from hotelapp.models import Hotel

# Create your models here.
class Review(models.Model):
    review=models.TextField()
    rating=models.FloatField(default=0)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.hotel.name+" 's review"

# select * from Review where hotel.id= 2

# select * from Review where hotel = (select * from Hotel where id =2)
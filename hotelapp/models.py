from django.db import models
from HotelReviews.s3_settings import PublicMediaStorage

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    location=models.TextField()
    image=models.ImageField(storage=PublicMediaStorage(), upload_to="media/", null=True,blank=True)
    rating=models.FloatField(default=0)
    number_of_reviews=models.IntegerField(default=0)

    def __str__(self):
        return self.name

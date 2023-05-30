import self as self
from django.db import models
from django.urls import reverse


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    dec = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def get_url(self):
        return reverse('movieapp:prod_cat_detail', args=[self.name, self.dec])

    def __str__(self):
        return self.name

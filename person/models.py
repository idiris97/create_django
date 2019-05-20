from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.DecimalField(decimal_places=0, max_digits=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_detail_view_url', kwargs={'name': self.name})

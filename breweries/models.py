from django.contrib.auth.models import User
from django.db import models
import uuid

class Brewery(models.Model):
    id = models.UUIDField(primary_key=True, default=lambda: str(uuid.uuid4()), editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    website = models.URLField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


    

class Review(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    description = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.brewery.name}'


# Create your models here.

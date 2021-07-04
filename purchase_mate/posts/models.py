from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    people=models.IntegerField(default=0, null=True)
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.title


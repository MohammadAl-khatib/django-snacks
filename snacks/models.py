from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    purchaser  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return (self.name)
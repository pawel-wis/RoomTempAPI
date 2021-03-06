from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Roomtemp(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

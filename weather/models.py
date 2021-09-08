from django.db import models
from django.db.models.base import Model
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Weather(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2,
                  validators=[MaxValueValidator(28), MinValueValidator(19)])
    humidity = models.DecimalField(max_digits=5, decimal_places=2,
                  validators=[MaxValueValidator(65), MinValueValidator(35)])
    form_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.temperature)
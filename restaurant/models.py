from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(validators=[MinValueValidator(1)])
    booking_date = models.DateTimeField(auto_now_add=True)


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.title}: {str(self.price)}'

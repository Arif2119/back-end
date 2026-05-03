from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    

    def __str__(self):
        return self.title
class Booking(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)
        NO_of_guests = models.IntegerField()
        Bookingdate = models.DateField()
        time = models.TimeField()
        

        def __str__(self):
            return f"{self.name} - {self.Bookingdate} {self.time}"
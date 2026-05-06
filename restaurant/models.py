from django.db import models

# Create your models here.
class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
class Booking(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)
        NO_of_guests = models.IntegerField()
        Bookingdate = models.DateField()
        time = models.TimeField()
        

        def __str__(self):
            return f"{self.name} - {self.Bookingdate} {self.time}"
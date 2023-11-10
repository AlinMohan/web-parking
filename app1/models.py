from django.db import models

# Create your models here.

class Users(models.Model):
    UserId = models.TextField()
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    VehicleNumber = models.TextField()
    Username = models.TextField()
    Password = models.TextField()


GENDER_CHOICES = (
        ('', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
)
class Staff(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.TextField(choices=GENDER_CHOICES, null=True, blank=True)
    Phone = models.IntegerField()
    Address=models.TextField()
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
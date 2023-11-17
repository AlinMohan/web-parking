from django.db import models

# Create your models here.

class Users(models.Model):
    # UserId = models.TextField()
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    VehicleNumber = models.TextField()
    Username = models.TextField(unique=True)
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

class ParkingSlot(models.Model):
    slot_number = models.IntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Slot {self.slot_number} - {'Available' if self.is_available else 'Occupied'}"  

class BookedSlot(models.Model):
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for Slot {self.slot.slot_number} by {self.user_name}"      
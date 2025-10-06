from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='timeslot',null=True)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True,blank=True)
    is_reserved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.service}-{self.date}-{self.start_time}"
    

class Booking(models.Model):
    timeslot = models.OneToOneField(TimeSlot,on_delete=models.CASCADE,related_name='booking')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.last_name}->{self.timeslot}"
    

class FeadBack(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.fullname



from django.db import models
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length = 30, null = True)
    email = models.EmailField()
    password = models.CharField(max_length = 10)

    def _str_(self):
        return str(self.id)


class Patient(models.Model):
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length = 30, null = True)
    email = models.EmailField() 
    contact_no = models.CharField(max_length = 10)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    address = models.TextField()
    doc = models.ForeignKey('Doctor',on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return str(self.id)

class PressureReading(models.Model):
    pat_id = models.ForeignKey('Patient', on_delete=models.CASCADE, null = False)
    mean_pressure = models.FloatField()
    hand = models.CharField(max_length=10)
    type_of_reading = models.CharField(max_length = 30)
    time = models.CharField(max_length = 30)

    def publish(self):
        self.created_date = timezone.now()
        self.save()




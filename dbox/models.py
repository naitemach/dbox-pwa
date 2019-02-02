from django.db import models
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length = 30, null = True)
    email = models.EmailField()
    password = models.CharField(max_length = 10)

    def _str_(self):
        return str(self.id)


class Patient(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length = 30, null = True)
    email = models.EmailField() 
    contact_no = models.CharField(max_length = 10)
    age = models.IntegerField()
    gender = models.CharField()
    address = models.TextField()
    doc_id = models.ForeignKey('Doctor')

    def _str_(self):
        return str(self.id)

class PressureReading(models.Model):
    id =  models.IntegerField(primary_key=True)
    mean_pressure = models.FloatField()
    hand = models.CharField()
    type_of_reading = models.IntegerField()

    def publish(self):
        self.created_date = timezone.now()
        self.save()



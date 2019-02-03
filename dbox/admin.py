from django.contrib import admin
from .models import Doctor,Patient,PressureReading

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PressureReading)


# Register your models here.

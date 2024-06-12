from django.db import models

class Owner(models.Model):
    CNIC = models.CharField(max_length=15, verbose_name='National ID Card Number', primary_key=True)
    full_name = models.CharField(max_length=60, verbose_name='Name of the Owner')
    phone_number = models.CharField(max_length=11)
    citizen_of = models.CharField(max_length=10, verbose_name='select the Country')
    address_of_owner = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.CNIC

# code from James
class VechicleDetail(models.Model):
    vehicle_number = models.CharField(max_length=18, verbose_name='Vehicle Plate Number', primary_key=True)
    owner = models.ForeignKey(Owner, max_length=100, on_delete=models.PROTECT)
    vehicle_name = models.CharField(max_length=30)
    model_number = models.CharField(max_length=15, verbose_name='Vehicle Model')
    chasis_number = models.CharField(max_length=20, verbose_name='Chasis Number')
    engine_number = models.CharField(max_length=20, verbose_name='Engine Number')
    vehicle_type = models.CharField(max_length=16, verbose_name='Type of Vehicle')
    
    
    def __str__(self):
        return self.vehicle_name
    
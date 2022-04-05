from django.db import models

# Create your models here.
class doctor_tb(models.Model):
    name = models.CharField(max_length=200)
    licens_no = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    
  



class patient_tb(models.Model):
    name = models.CharField(max_length=200)
    age= models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)    


class booking_tb(models.Model):
   
    description= models.CharField(max_length=200)
    time= models.CharField(max_length=200)
    date= models.CharField(max_length=200)


    pid=models.ForeignKey(patient_tb,on_delete=models.CASCADE)
    did=models.ForeignKey(doctor_tb,on_delete=models.CASCADE)    

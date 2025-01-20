from django.db import models


class Aadhar(models.Model):
   aadhar_no = models.IntegerField(unique=True)
   created_by = models.CharField(max_length=50)
   created_data = models.DateField()
   def __str__(self):
      return str(self.aadhar_no)

class userProfile(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField()
   contact = models.IntegerField()
   aadhar = models.OneToOneField(Aadhar,on_delete=models.PROTECT)
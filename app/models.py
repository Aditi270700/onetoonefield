from django.db import models

# one to one field
# class Aadhar(models.Model):
#    aadhar_no = models.IntegerField(unique=True)
#    created_by = models.CharField(max_length=50)
#    created_data = models.DateField()
#    def __str__(self):
#       return str(self.aadhar_no)

# class userProfile(models.Model):
#    name = models.CharField(max_length=50)
#    email = models.EmailField()
#    contact = models.IntegerField()
#    aadhar = models.OneToOneField(Aadhar,on_delete=models.PROTECT)
'''
class Departmant(models.Model):
   dep_name = models.CharField(max_length=50,unique=True)
   dep_des = models.TextField()
   dep_hod = models.CharField(max_length=50)
   def __str__(self):
      return self.dep_name

class Student(models.Model):
   student_name = models.CharField(max_length=50)
   student_email = models.EmailField()
   student_dep = models.ForeignKey(Departmant,on_delete=models.PROTECT,to_field="dep_name")
   student_roll = models.IntegerField()
   def __str__(self):
      return self.student_name
'''
# many to many
v_nm=[('Tata','Tata'),('BMW','BMW'),('Audi','Audi')]
f_nm = [('Petrol','petrol'),('Desel','Desel'),('CNG','CNG'),('EV','EV')]
class Vehicle(models.Model):
   v_name = models.CharField(max_length=50,choices=v_nm)
   def __str__(self):
      return self.v_name
class Fuel(models.Model):
   f_name=models.CharField(max_length=50,choices=f_nm)
   v_name=models.ManyToManyField(Vehicle)
   def __str__(self):
      return self.f_name

      

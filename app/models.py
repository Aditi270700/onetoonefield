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

class Departmant(models.Model):
   dep_name = models.CharField(max_length=50)
   dep_des = models.TextField()
   dep_hod = models.CharField(max_length=50)
   def __str__(self):
      return self.dep_name

class Student(models.Model):
   student_name = models.CharField(max_length=50)
   student_email = models.EmailField()
   student_dep = models.CharField(max_length=50)
   student_roll = models.IntegerField()
   def __str__(self):
      return self.student_name
from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.email
    

class Lectures(models.Model):

    Lecture_ID = models.IntegerField(primary_key=True)
    Faculty_Name = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return self.Faculty_Name
    

class Booking(models.Model):
    
    
    
    date = models.DateField()
    time = models.TimeField()
    lecture = models.CharField(max_length=254)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=12 , default="" , blank=True)
    college = models.TextField(max_length=300 ,  blank=True)
    branch = models.TextField(max_length=200 ,  blank=True )

    def __str__(self):
        return self.name
    
   

   
    
    
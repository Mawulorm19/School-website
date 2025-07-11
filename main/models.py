from django.db import models

class SchoolInfo(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to = 'logos/')
    about = models.TextField()
    
    def __str__(self):
        return self.name
    
class Announcement(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    
class Course(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    featured = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
class ContactInfo(models.Model):
    address = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    
    def __self__(self):
        return self.email

# Create your models here.

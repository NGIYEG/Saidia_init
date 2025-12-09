from django.db import models

# Create your models here.
class Supporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
   

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.firstname
    
class Blogpost(models.Model):
   tittle = models.CharField(max_length=200)
   content = models.TextField()     
   date_posted = models.DateTimeField(auto_now_add=True)
   author = models.CharField(max_length=100)
   blogimage= models.ImageField(upload_to='blog_images/')

   def __str__(self):
        return self.tittle
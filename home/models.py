from django.db import models
from django.contrib.auth.models import User

# makemigrations - create changes and store in a file
# migrate - apply the pending changes in the file created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Credentials(models.Model):
    name = models.CharField(max_length=122, unique=False)
    email = models.CharField(max_length=122, unique=True)
    password = models.CharField(max_length=122, unique=False)
    priv = models.IntegerField(null=True, default=0)
    def __str__(self):
        #return f'{self.name} {self.email} {self.password}' 
        return self.name
    
class Forum(models.Model):
    name = models.CharField(max_length=122)
    topic = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=122)
    body = models.CharField(max_length=122)
    mail = models.CharField(max_length=100, null=True)
    
    def __str__(self): 
        return self.name

class Event(models.Model):
    head = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    month = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    email = models.CharField(max_length=200, null=True)
    def str(self):
        return self.head    
    
class Alert(models.Model):
    topic = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    body = models.CharField(max_length=1000)
    disp = models.BooleanField(null=True, default=False)
    def str(self):
        return self.topic
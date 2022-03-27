from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class certificates(models.Model):
    title=models.CharField(max_length=50)
    img1=models.ImageField(upload_to ='apps/')

class clients(models.Model):
    title=models.CharField(max_length=100)
    img1=models.ImageField(upload_to ='apps/')

class ownedCompanies(models.Model):
    title=models.CharField(max_length=50)
    link=models.URLField(max_length=200)
    img1=models.ImageField(upload_to ='apps/')

class aboutUs(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    img1=models.ImageField(upload_to ='apps/static/images')

class footer(models.Model):
    address=models.CharField(max_length=150)
    mail1=models.URLField(max_length=300)
    mail2=models.URLField(max_length=300)
    mail3=models.URLField(max_length=300)
    phone1=models.CharField(max_length=50)
    phone2=models.CharField(max_length=50)


class seaJob(models.Model):
    title=models.CharField(max_length=100)
    which=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)

class landJob(models.Model):
    title=models.CharField(max_length=100)
    which=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
from django.db import models

# Create your models here.
class Contactu(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    city=models.CharField(max_length=100)
    reasonforcontact=models.TextField()
    def __str__(self):
        return self.name
class Applicant(models.Model):
    fullname=models.CharField(max_length=50)
    applyfor=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    emailid=models.EmailField()
    resume=models.FileField(upload_to="cvs/%Y/%m/%d/")
    def __str__(self):
        return self.fullname
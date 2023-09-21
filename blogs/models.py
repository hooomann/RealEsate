from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    by=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    article=models.TextField()
    subheading=models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    thumbnail=models.ImageField(upload_to='thumbnails/%Y/%m/%d/')
    def __str__(self):
        return self.title

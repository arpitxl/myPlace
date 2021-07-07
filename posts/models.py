from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    desc = models.TextField()
    photo = models.ImageField(upload_to='posts/images')
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.title
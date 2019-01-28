from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    guide = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    content = models.TextField()


    class Meta:
        db_table = 'blog'

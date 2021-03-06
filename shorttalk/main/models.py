from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, related_name = "author")
    content = models.CharField(max_length = 50, blank = False)

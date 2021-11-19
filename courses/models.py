from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

# Create your models here.

class Courses(models.Model):
   id_course = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   name = models.CharField(max_length=255)
   author = models.CharField(max_length=255)
   release_year = models.IntegerField()
   description = models.TextField()
   url = models.TextField()
   is_free = models.BooleanField()
   value = models.DecimalField(decimal_places=2, max_digits=10)
   created_at = models.DateField(auto_now_add=True)
   owner = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
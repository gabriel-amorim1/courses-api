from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator

from courses.models import Courses

# Create your models here.
class Ratings(models.Model):
   id_rating = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   value = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
   created_at = models.DateField(auto_now_add=True)
   owner = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
   course = models.ForeignKey(Courses, related_name='ratings', on_delete=models.CASCADE)
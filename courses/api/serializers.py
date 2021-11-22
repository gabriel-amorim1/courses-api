from django.db.models import fields
from rest_framework import serializers
from courses import models

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Courses
        fields = '__all__'
        read_only_fields = ('owner',)
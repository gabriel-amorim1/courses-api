from rest_framework import serializers
from courses.models import Courses
from ratings import models

class RatingsSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())
    
    class Meta:
        model = models.Ratings
        fields = '__all__'
        read_only_fields = ('owner', 'course')
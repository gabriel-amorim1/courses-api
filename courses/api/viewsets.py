from rest_framework import viewsets
from courses.api import serializers
from courses import models

class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CoursesSerializer
    queryset = models.Courses.objects.all()
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.api import serializers
from courses import models

class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.CoursesSerializer
    queryset = models.Courses.objects.all()
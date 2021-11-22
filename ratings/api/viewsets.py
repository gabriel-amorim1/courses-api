from django.db.models.aggregates import Avg, Count, Sum
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from courses.models import Courses

from ratings.api import serializers
from ratings import models

class RatingsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.RatingsSerializer
    queryset = models.Ratings.objects.all()

    def perform_create(self, serializer):
        aggregated_ratings = models.Ratings.objects.filter(course=self.request.data['course']).aggregate(        
            count=Count('id_rating'), 
            total_value=Sum('value')
        )
        
        new_count = aggregated_ratings['count'] + 1
        
        if aggregated_ratings['total_value'] is not None :
            new_ratings_value = (aggregated_ratings['total_value'] + self.request.data['value']) / new_count
        else :
            new_ratings_value = self.request.data['value'] / new_count

        course = Courses.objects.filter(pk=self.request.data['course'])

        course.update(rating=new_ratings_value, quantity_of_ratings=new_count)

        serializer.validated_data['owner'] = self.request.user
        serializer.save()

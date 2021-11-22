from django.db.models.aggregates import Count, Sum
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from courses.models import Courses
from rest_framework.serializers import ValidationError
from rest_framework.response import Response

from ratings.api import serializers
from ratings import models

class RatingsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.RatingsSerializer
    queryset = models.Ratings.objects.all()

    def perform_create(self, serializer):
        user_course_rating = models.Ratings.objects.filter(course=self.request.data['course'], owner=self.request.user.pk)

        if user_course_rating :
            raise ValidationError({"conflict": "You already rated this course"})

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
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = self.request.user

        if not user.pk == instance.owner.pk:
            raise ValidationError({"authorize": "You dont have permission for this resource."})

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
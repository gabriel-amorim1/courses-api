from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status

from courses.api import serializers
from courses import models

class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.CoursesSerializer
    queryset = models.Courses.objects.all()

    def perform_create(self, serializer):
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
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = self.request.user

        if not user.pk == instance.owner.pk:
            raise ValidationError({"authorize": "You dont have permission for this resource."})

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

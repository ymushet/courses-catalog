from rest_framework import viewsets, permissions

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    View set for Course Model
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny, ]

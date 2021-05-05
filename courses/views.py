from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from courses.filters import CourseViewFilter
from courses.models import Course
from courses.permissions import IsAuthorOrReadOnly
from courses.serializers import CourseSerializer, UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    View set for Course Model
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'author', ]
    filterset_class = CourseViewFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'courses': reverse('courses-list', request=request, format=format)
    })

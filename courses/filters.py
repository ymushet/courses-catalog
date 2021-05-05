from django_filters import FilterSet
from django_filters import filters

from courses.models import Course


class CourseViewFilter(FilterSet):
    start_at = filters.DateTimeFilter(lookup_expr='gte')
    end_at = filters.DateTimeFilter(lookup_expr='lte')

    class Meta:
        model = Course
        fields = ['start_at', 'end_at']

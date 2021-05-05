from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Course
        fields = ['id', 'name', 'start_at', 'end_at', 'lectures', 'author']

    def validate(self, attrs):
        if attrs['start_at'] >= attrs['end_at']:
            raise serializers.ValidationError({"end_at": "end date must occur after begin"})
        if attrs['start_at'] <= timezone.now():
            raise serializers.ValidationError({'start_at': 'Start date must be in future'})
        return super(CourseSerializer, self).validate(attrs)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, view_name='courses-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'courses']

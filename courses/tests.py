import datetime

import pytz
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from courses.models import Course
from courses.serializers import CourseSerializer

client = Client()


class CourseModelTestCase(TestCase):
    """
    Test class for Course model
    """

    def setUp(self):
        Course.objects.create(
            name='Yalantis Python School',
            lectures=10,
            start_at=datetime.datetime(2021, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
            end_at=datetime.datetime(2021, 8, 14, 21, 0, 0, tzinfo=pytz.UTC),
        )

    def test_repr(self):
        course = Course.objects.get(name='Yalantis Python School')
        self.assertEqual(str(course), f'{course.name} course has {course.lectures} lectures')


class CoursesViewSetTestCase(TestCase):
    def setUp(self):
        Course.objects.create(
            name='Yalantis Golang school',
            lectures=10,
            start_at=datetime.datetime(2021, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
            end_at=datetime.datetime(2021, 8, 14, 21, 0, 0, tzinfo=pytz.UTC),
        )

        Course.objects.create(
            name='Yalantis JavaScript school',
            lectures=10,
            start_at=datetime.datetime(2021, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
            end_at=datetime.datetime(2021, 8, 14, 21, 0, 0, tzinfo=pytz.UTC),
        )

    def test_list_view(self):
        response = client.get(reverse('courses-list'))
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

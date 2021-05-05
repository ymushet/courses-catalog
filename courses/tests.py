import datetime

import pytz
from django.contrib.auth.models import User
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
        admin = User.objects.create_superuser('admin', 'myemail@test.com', 'pass123')
        Course.objects.create(
            author=admin,
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
        admin = User.objects.create_superuser('admin', 'myemail@test.com', 'pass123')

        Course.objects.create(
            author=admin,
            name='Yalantis Golang school',
            lectures=10,
            start_at=datetime.datetime(2022, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
            end_at=datetime.datetime(2023, 8, 14, 21, 0, 0, tzinfo=pytz.UTC),
        )

        Course.objects.create(
            author=admin,
            name='Yalantis JavaScript school',
            lectures=10,
            start_at=datetime.datetime(2022, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
            end_at=datetime.datetime(2023, 8, 14, 21, 0, 0, tzinfo=pytz.UTC),
        )

    def test_list_view(self):
        admin = User.objects.get(username='admin')
        client.force_login(user=admin)
        response = client.get(reverse('courses-list'))
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_view(self):
        admin = User.objects.get(username='admin')
        client.force_login(user=admin)
        course = Course.objects.create(author=admin,
                                       lectures=10,
                                       name='My cool course',
                                       start_at=datetime.datetime(2022, 5, 14, 19, 0, 0, tzinfo=pytz.UTC),
                                       end_at=datetime.datetime(2023, 8, 14, 21, 0, 0, tzinfo=pytz.UTC))
        response = client.get(reverse('courses-detail', kwargs={'pk': course.id}))
        serializer = CourseSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_authorized_post(self):
        payload = {
            "name": 'My second cool course',
            "lectures": 10,
            "start_at": "2021-05-17T19:00:00Z",
            "end_at": "2021-08-30T21:00:00Z",
        }
        response = client.post('/courses/', data=payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_post(self):
        admin = User.objects.get(username='admin')
        client.force_login(user=admin)
        payload = {
            "name": 'My third cool course',
            "lectures": 10,
            "start_at": "2021-05-17T19:00:00Z",
            "end_at": "2021-08-30T21:00:00Z",
        }
        response = client.post('/courses/', data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.filter(name='My third cool course').exists(), True)

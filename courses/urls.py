from django.urls import path
from rest_framework import routers

from courses.views import CourseViewSet, UserList, UserDetail, api_root

router = routers.SimpleRouter()

router.register('courses', CourseViewSet, basename='courses')

urlpatterns = router.urls

urlpatterns.append(path('', api_root)),
urlpatterns.append(path('users', UserList.as_view()))
urlpatterns.append(path('users/<int:pk>', UserDetail.as_view()))

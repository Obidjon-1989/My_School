from django.urls import path, include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'pupils', PupilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]



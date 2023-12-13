"""
URL mappings for the recipe app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from department import views


router = DefaultRouter()
router.register('departments', views.UniversityDepartmentViewSet)

app_name = 'department'

urlpatterns = [
    path('', include(router.urls)),
]

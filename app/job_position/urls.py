"""
URL mappings for the job position app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from job_position import views


router = DefaultRouter()
router.register('positions', views.JobPositionViewSet)

app_name = 'job_position'

urlpatterns = [
    path('', include(router.urls)),
]

"""
URL mappings for the rating app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from rating import views


router = DefaultRouter()
router.register('ratings', views.RatingReviewViewSet)

app_name = 'rating'

urlpatterns = [
    path('', include(router.urls)),
]

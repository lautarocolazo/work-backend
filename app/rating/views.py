"""
Views for rating API.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import RatingReview
from rating import serializers


class RatingReviewViewSet(viewsets.ModelViewSet):
    """View to manage job position API."""
    serializer_class = serializers.RatingReviewSerializer
    queryset = RatingReview.objects.all()
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     return self.queryset.filter(user=self.request.user).order_by('-id')

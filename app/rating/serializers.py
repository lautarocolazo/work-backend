"""
Serializer for rating API.
"""
from rest_framework import serializers

from core.models import RatingReview


class RatingReviewSerializer(serializers.ModelSerializer):
    """Rating serializer."""

    class Meta:
        model = RatingReview
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

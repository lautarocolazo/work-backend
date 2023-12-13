"""
Serializer for job position API.
"""
from rest_framework import serializers

from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    """Job position serializer."""

    class Meta:
        model = JobPosition
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

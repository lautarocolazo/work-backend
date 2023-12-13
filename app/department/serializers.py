"""
Serializer for deparment API.
"""
from rest_framework import serializers

from core.models import UniversityDepartment


class UniversityDepartmentSerializer(serializers.ModelSerializer):
    """University department serializer."""

    class Meta:
        model = UniversityDepartment
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

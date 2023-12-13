"""
Views for Job Position API.
"""
from rest_framework import viewsets
# from rest_restframework.authentication import TokenAuthentication
# from rest_restframework.permissions import IsAuthenticated

from core.models import JobPosition
from job_position import serializers


class JobPositionViewSet(viewsets.ModelViewSet):
    """View to manage job position API."""
    serializer_class = serializers.JobPositionSerializer
    queryset = JobPosition.objects.all()

    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     return self.queryset.filter(user=self.request.user).order_by('-id')

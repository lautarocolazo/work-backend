"""
Views for the user API.
"""

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from user.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class GetUserView(generics.RetrieveAPIView):
    """Retrieve the current user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['POST'])
def login(request):
    user = get_object_or_404(get_user_model(), email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = get_user_model().objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        return Response({"token": token.key, "user": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test_token(request):
    return Response({})

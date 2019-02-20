from .models import Review # Import our Review model
from .serializers import ReviewSerializer # Import the serializer we just created

# Import django rest framework functions

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ReviewViewSet(viewsets.ModelViewSet): # Create a class based view
    """
    API endpoint that allows Reviews to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all() # Select all taks
    serializer_class = ReviewSerializer # Serialize data

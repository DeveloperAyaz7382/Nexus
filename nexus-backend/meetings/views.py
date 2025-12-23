from rest_framework import generics
from .models import Meeting
from .serializers import MeetingSerializer

class MeetingCreateView(generics.CreateAPIView):
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        # conflict detection logic
        serializer.save()

class MeetingListView(generics.ListAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

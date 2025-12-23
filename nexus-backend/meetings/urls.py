from django.urls import path
from .views import MeetingCreateView, MeetingListView  # make sure these exist

urlpatterns = [
    path('create/', MeetingCreateView.as_view(), name='meeting-create'),
    path('list/', MeetingListView.as_view(), name='meeting-list'),
]

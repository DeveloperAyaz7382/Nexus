from django.urls import path
from .views import DocumentUploadView, DocumentListView  # make sure these exist

urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('list/', DocumentListView.as_view(), name='document-list'),
]

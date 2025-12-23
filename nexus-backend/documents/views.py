from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer

class DocumentUploadView(generics.CreateAPIView):
    serializer_class = DocumentSerializer

class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

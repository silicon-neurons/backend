from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer, LensSerializer
from .models import Post, Lens
#TODO Add Correction

class PostListView(generics.ListAPIView):
    """
    Provides a GET method for posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LensListView(generics.ListAPIView):
    """
    Provides a GET method for lenses.
    """
    queryset = Lens.objects.all()
    serializer_class = LensSerializer

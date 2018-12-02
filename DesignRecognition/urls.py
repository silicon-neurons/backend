from django.urls import path
from .views import PostListView, LensListView
# TODO Add Correction

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-all'),
    path('lens/', LensListView.as_view(), name='lens-all'),
]
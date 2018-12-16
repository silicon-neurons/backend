from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, LensListView
# TODO Add Correction

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostCreateView.as_view(), name='post-new'),
    path('lens/', LensListView.as_view(), name='lens-list'),
]

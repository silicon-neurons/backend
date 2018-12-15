from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, LensListView, LocationLimitedListView
# TODO Add Correction

urlpatterns = [
    #? Is this the best way to send floats through URL? Maybe match exact pattern?
    path('posts/<str:x1>/<str:y1>/<str:x2>/<str:y2>/', LocationLimitedListView.as_view(), name='posts-limited'),
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostCreateView.as_view(), name='post-new'),
    path('lens/', LensListView.as_view(), name='lens-list'),
]
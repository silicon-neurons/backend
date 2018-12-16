from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import PostSerializer, SimplePostSerializer, LensSerializer
from .models import Post, Lens
#TODO Add Correction

class PostListView(generics.ListAPIView):
    """
    Provides a GET method for posts as pins.
    """
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer

class LocationLimitedListView(generics.ListAPIView):
    """
    Provides a GET method for posts as pins within a bounding rectangle.
    """
    queryset = Post.objects.all()
    serializer_class = SimplePostSerializer
     def get(self, request, *args, **kwargs):
        try:
            x1,y1,x2,y2 = float(kwargs["x1"]),float(kwargs["y1"]),float(kwargs["x2"]),float(kwargs["y2"])
            bounded_posts = self.queryset.filter(geo_latitude__gt=x1, geo_longitude__gt=y1, geo_latitude__lt=x2, geo_longitude__lt=y2)
            return Response(SimplePostSerializer(bounded_posts, many=True).data)
        except ValueError:
            return Response(
                data={
                    "message": "URL parameters were not formatted as floats."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class PostCreateView(generics.CreateAPIView):
    """
    Provides a POST method for creating new posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # TODO Validate details
    def post(self, request, *args, **kwargs):
        a_post = Post.objects.create(
            image = request.data["image"],
            desc = request.data["desc"],
            design = request.data["design"],
            user = None, #! Change when auth is done
            lens = Lens.objects.get(title=request.data["lens"]),
            geo_latitude = request.data["geo_latitude"],
            geo_longitude = request.data["geo_longitude"]
        )
        return Response(
            data=PostSerializer(a_post).data,
            status=status.HTTP_201_CREATED
        )

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides GET, PUT and DELETE methods for a single, detailed post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_post = self.queryset.get(pk=kwargs["pk"])
            return Response(PostSerializer(a_post).data)
        except Post.DoesNotExist:
            return Response(
                data={
                    "message": "Post with id {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    # TODO Validate details
    def put(self, request, *args, **kwargs):
        try:
            a_post = self.queryset.get(pk=kwargs["pk"])
            serializer = PostSerializer()
            updated_post = serializer.update(a_post, request.data)
            return Response(PostSerializer(updated_post).data)
        except Post.DoesNotExist:
            return Response(
                data={
                    "message": "Post with id {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_post = self.queryset.get(pk=kwargs["pk"])
            a_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(
                data={
                    "message": "Post with id {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class LensListView(generics.ListAPIView):
    """
    Provides a GET method for lenses.
    """
    queryset = Lens.objects.all()
    serializer_class = LensSerializer

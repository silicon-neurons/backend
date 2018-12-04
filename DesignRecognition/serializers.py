from rest_framework import serializers
from .models import Post, Lens
# TODO Add Correction
# TODO Add Tag later, maybe

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'design', 'lens', 'geo_latitude', 'geo_longitude')

class LensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = ('id', 'title', 'desc', 'timestamp')

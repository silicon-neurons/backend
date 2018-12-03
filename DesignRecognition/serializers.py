from rest_framework import serializers
from .models import Post, Lens
# TODO Add Correction
# TODO Add Tag later, maybe

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'desc', 'design', 'lens', 'geo_latitude', 'geo_longitude', 'timestamp')

class LensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = ('title', 'desc', 'timestamp')

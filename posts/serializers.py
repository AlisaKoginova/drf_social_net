from posts.models import Post, Like
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        likes = serializers.SerializerMethodField('get_likes_num')
        fields = ('author', 'title', 'description', 'pub_date', 'get_likes_num')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('author', 'post', 'created')

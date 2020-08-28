from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        likes = serializers.SerializerMethodField('get_likes_num')
        fields = ('author', 'title', 'description', 'pub_date', 'liked_by', 'get_likes_num')

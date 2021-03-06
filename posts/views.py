
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer


class LikeListView(ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = (AllowAny, )
    queryset = Like.objects.order_by('-created')
    pagination_class = LimitOffsetPagination


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-pub_date')
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'author': request.user.pk,
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'Post created successfully',
        }

        return Response(response, status=status_code)


class PostLikeView(RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, post_id):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        if Like.objects.filter(author=request.user, post=post).all():
            Like.objects.filter(author=request.user, post=post).delete()
        else:
            like = Like.objects.create(author=request.user, post=post)
            like.save()
        post.save()
        status_code = status.HTTP_200_OK
        response = {
            'success': True,
            'status code': status_code,
            'message': 'Post liked/reliked successfully',
            'likes': post.get_likes_num(),
        }

        return Response(response, status=status_code)
    

class LikeAnalyticsView(ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):

        from_date = self.kwargs['from_date']
        to_date = self.kwargs['to_date']
        filtered = Like.objects.filter(created__range=[from_date, to_date])

        return filtered

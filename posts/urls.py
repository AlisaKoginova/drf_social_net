from django.urls import path, re_path

from .views import (
    PostListView,
    PostCreateView,
    PostLikeView,
    LikeListView,
    LikeAnalyticsView,
)

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('create-post/', PostCreateView.as_view()),
    path('like-post/<int:post_id>/', PostLikeView.as_view()),
    path('likes/', LikeListView.as_view()),
    re_path(r'^date_from=(?P<from_date>\d{4}-\d{2}-\d{2})&date_to=(?P<to_date>\d{4}-\d{2}-\d{2})/$', LikeAnalyticsView.as_view())
]

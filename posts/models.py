from django.db import models
from django.utils import timezone
from users.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=1000, unique=False)
    pub_date = models.DateTimeField(default=timezone.now())

    def get_likes_num(self):
        return Like.objects.filter(post=self).count()


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'post',)


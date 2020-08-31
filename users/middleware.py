from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from users.models import User


class SetLastVisitMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.pk).update(last_activity=now())
        return response


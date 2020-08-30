from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

urlpatterns = [
    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),

]

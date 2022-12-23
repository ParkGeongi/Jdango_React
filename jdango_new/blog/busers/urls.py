from django.urls import re_path as url

from blog.busers import views

urlpatterns = [
    url(r'blog-signup',views.blog_login)
]
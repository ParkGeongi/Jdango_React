from django.urls import re_path as url

from security.seq_users import views

urlpatterns = [
    url(r'seq_users',views.list),
    url(r'seq-users',views.suser_views),
    url(r'login',views.login)
]
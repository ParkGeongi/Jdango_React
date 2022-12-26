from django.urls import re_path as url

from security.seq_users import views

urlpatterns = [
    url(r'seq_users',views.suser_views)
]
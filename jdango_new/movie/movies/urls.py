from django.urls import re_path as url

from movie.movies import views


urlpatterns = [
    url(r'fake-images',views.fake_images),

    url(r'blow-up-face',views.faces_blow_up)
]
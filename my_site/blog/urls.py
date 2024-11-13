from django.urls import path

from . import views  # dot represents the current folder

urlpatterns = [
    path("", views.starting_page, name="starting-page"),   # path for empty page
    path("posts", views.posts, name="posts-page"),  # path for posts page
    path("posts/<slug:slug>", views.post_detail, name="posts-detail-page")
]

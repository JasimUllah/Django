from django.urls import path

from . import views  # dot represents the current folder

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),   # path for empty page
    path("posts", views.AllPosts.as_view(), name="posts-page"),  # path for posts page
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="posts-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]

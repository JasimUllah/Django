from django.test import TestCase

from . import views

# Create your tests here.

urlpatterns = [
    path("", views.CreateProfileView.as_view())
]
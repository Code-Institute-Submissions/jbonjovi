from django.urls import path
from .views import BlogView, PostDetails

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetails.as_view(), name='post_details'),
]

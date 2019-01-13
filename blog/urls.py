from django.urls import path
from .views import (
            PostListView,
            PostDetailView,
            PostCreateView,
            PostUpdateView,
            PostDeleteView
)
from . import views




urlpatterns = [
    path('' , PostListView.as_view() , name='home'),
    path('post/create/' , PostCreateView.as_view() , name='create'),
    path('post/<int:pk>/' , PostDetailView.as_view() , name='detail'),
    path('post/<int:pk>/update/' , PostUpdateView.as_view() , name='update'),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view() , name='delete'),
    path('about/', views.about, name='about'),
]

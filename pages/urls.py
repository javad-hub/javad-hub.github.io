from django.urls import path
from .views import PaintDetailView, PaintListView, CommentPageView, LikeView, AboutPageView, VideoPageView
urlpatterns = [
    path('pages/',PaintListView.as_view(),name="list"),
    path('<int:pk>',PaintDetailView.as_view(),name="detail"),
    path('comments/',CommentPageView.as_view(),name="comment"),
    path('like/<int:pk>',LikeView, name="like_paint"),
    path('about/',AboutPageView.as_view(),name="about"),
    path('videos/',VideoPageView.as_view(), name="video"),
]
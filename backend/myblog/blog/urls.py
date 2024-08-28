# blog/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('tag/<int:tag_id>/', views.tag_posts, name='tag_posts'),
     path('api/', include(router.urls)),
]

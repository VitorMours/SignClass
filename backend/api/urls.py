from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                            TokenRefreshView,
                                            TokenVerifyView)

from .views.user_views import UserView, UserDetailView
from .views.sign_views import SignView
from .views.video_views import VideoView
from .views.auth_views import CustomTokenObtainPairView

urlpatterns = [
    # path('auth/singin'),
    path('auth/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('users/<int:pk>/profile', UserDetailView.as_view(), name='user_profile'),
    path('users/<int:pk>', UserDetailView.as_view(), name='singular_user'),
    path('users', UserView.as_view(), name='users'),
    path('signs', SignView.as_view(), name='signs'),
    path('videos', VideoView.as_view(), name='videos'),
    path('knowledge_sector', VideoView.as_view(), name='knowledge_sector'),
    
]
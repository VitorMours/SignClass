from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
import rest_framework_nested.routers as routers 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import UserViewSet, VideoViewSet, UserVideoViewSet

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="LibraChat API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jvrezendemoura@gmail.com"),
        license=openapi.License(name="BSD License"),
   ),
   public=True,
)


router.register(r'users', UserViewSet, basename='user')
router.register(f'videos', VideoViewSet, basename='video')

user_routes = routers.NestedDefaultRouter(router, f'users', lookup='user')
user_routes.register(r'videos', UserVideoViewSet, basename='user-videos')

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('', include(user_routes.urls)),
]
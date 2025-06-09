from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from listings.views import PropertyViewSet, ImageViewSet, FavoriteViewSet, InquiryViewSet, UserViewSet

# For Swagger/Redoc
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'inquiries', InquiryViewSet)
router.register(r'users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version='v1',
        description="API documentation for Real Estate project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # API docs:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

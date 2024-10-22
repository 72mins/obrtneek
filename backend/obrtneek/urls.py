from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from obrtneek_app import urls as app_urls
from obrtneek_app.views.user import CustomRefreshView, CustomTokenPairView

urlpatterns = [
    path("", include(app_urls)),
    path("admin/", admin.site.urls),
    # Auth
    path("api/token/refresh/", CustomRefreshView.as_view(), name="token_refresh"),
    path("api/token/", CustomTokenPairView.as_view(), name="token_obtain_pair"),
    # DRF Spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

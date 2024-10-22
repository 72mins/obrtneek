from rest_framework.routers import DefaultRouter

from obrtneek_app.views.company import CompanyViewSet

router = DefaultRouter()

router.register("company", CompanyViewSet, basename="company")

urlpatterns = [
    *router.urls,
]

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from obrtneek_app.models.company import Company
from obrtneek_app.serializers.company import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Company.objects.all()

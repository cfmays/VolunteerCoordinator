from rest_framework.viewsets import ModelViewSet
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
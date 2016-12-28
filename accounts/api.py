from rest_framework.viewsets import ModelViewSet
from .models import Organization, Role
from .serializers import OrganizationSerializer, RoleSerializer


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

class RoleViewSet(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

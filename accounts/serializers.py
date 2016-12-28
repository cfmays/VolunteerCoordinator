from rest_framework import serializers
from .models import Organization
from .models import Role

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = (
            'name',
            'category',
        )

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = (
            'title',
            'category',
        )

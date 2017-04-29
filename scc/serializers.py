from rest_framework.serializers import ModelSerializer

from .models import Specialist, Organization, Order, Equipment


class SpecialistSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        exclude = ('user',)


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        exclude = ('user',)


class OrderSerializer(ModelSerializer):
    organization = OrganizationSerializer(source='equipment.organization', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

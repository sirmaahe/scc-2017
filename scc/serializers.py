from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

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
    equipment = PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    specialist = PrimaryKeyRelatedField(queryset=Specialist.objects.all())

    class Meta:
        model = Order
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    organization = PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = Equipment
        fields = '__all__'

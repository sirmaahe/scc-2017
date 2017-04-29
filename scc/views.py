from django.core.exceptions import ValidationError
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from .serializers import SpecialistSerializer, OrganizationSerializer, OrderSerializer, EquipmentSerializer
from .models import Order, Equipment


class UserExtensionCRUD(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView
):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SpecialistView(UserExtensionCRUD):
    serializer_class = SpecialistSerializer

    def get_object(self):
        instance = getattr(self.request.user, 'specialist')
        if not instance:
            raise ValidationError
        return instance


class OrganizationView(UserExtensionCRUD):
    serializer_class = OrganizationSerializer

    def get_object(self):
        instance = getattr(self.request.user, 'organization')
        if not instance:
            raise ValidationError
        return instance


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'specialist'):
            return Order.objects.all()

        return Order.objects.filter(equipment__organization=self.request.user.organization)


class EquipmentViewSet(ModelViewSet):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'specialist'):
            return Equipment.objects.all()

        return Equipment.objects.filter(organization=self.request.user.organization)

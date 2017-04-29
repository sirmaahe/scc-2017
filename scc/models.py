from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    actual_address = models.CharField(max_length=256)
    contacts = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)


class Specialist(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    geodata = models.CharField(max_length=128, null=True)


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128)
    program = models.CharField(max_length=128)
    operational_system = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, models.CASCADE)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    work_begin_at = models.DateTimeField(null=True, blank=True)
    work_complete_at = models.DateTimeField(null=True, blank=True)
    equipment = models.ForeignKey(Equipment, models.CASCADE)
    description = models.TextField(null=True, blank=True)
    specialist = models.ForeignKey(Specialist, models.CASCADE, null=True)

from django.db import models
from django.contrib.auth.models import User


class OrganizationProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    actual_address = models.CharField(max_length=256)
    contacts = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)


class Specialist(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128)
    program = models.CharField(max_length=128)
    operational_system = models.CharField(max_length=128)
    organization = models.ForeignKey(OrganizationProfile)


class 
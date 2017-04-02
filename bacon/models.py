from __future__ import unicode_literals

from django.db import models


class Design(models.Model):
    """
    dummy class 1
    """
    name = models.CharField(max_length=255)


class DesignFeatures(models.Model):
    """
    dummy class 2
    """
    lead_free = models.BooleanField()
    thickness = models.DecimalField(decimal_places=4, max_digits=10)

    """List of board features"""
    design = models.OneToOneField(
        Design,
        on_delete=models.CASCADE,
        related_name='features',
    )

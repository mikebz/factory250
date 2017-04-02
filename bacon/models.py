from __future__ import unicode_literals

from django.db import models


class Design(models.Model):
    """
    dummy class 1
    """
    name = models.CharField(max_length=255)

    def get_thickness(self):
        """
        an example getter
        """
        try:
            return self.features.thickness
        except DesignFeatures.DoesNotExist:
            return None

    def set_thickness(self, thickness):
        """
        an example setter
        """
        try:
            self.features.thickness = thickness
            self.features.save()
        except DesignFeatures.DoesNotExist:
            self.features = DesignFeatures.objects.create(
                design=self, thickness=thickness)


class DesignFeatures(models.Model):
    """
    dummy class 2
    """
    lead_free = models.BooleanField(default=True, )
    thickness = models.DecimalField(decimal_places=4, max_digits=10, default=0)

    """List of board features"""
    design = models.OneToOneField(
        Design,
        on_delete=models.CASCADE,
        related_name='features',
    )

import factory
import models


class DesignFeaturesFactory(factory.django.DjangoModelFactory):
    """
    factory for the main class
    """
    class Meta(object):
        """
        meta
        """
        model = models.DesignFeatures


class DesignFactory(factory.django.DjangoModelFactory):
    """
    factory for the related class
    """

    class Meta(object):
        """
        meta
        """
        model = models.Design

    features = factory.RelatedFactory(DesignFeaturesFactory, 'design')

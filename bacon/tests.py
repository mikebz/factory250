from django.test import TestCase
import factories


class BaconTests(TestCase):
    """
    simple test that shows the bug
    """

    def test_bacon(self):
        """
        test case - we are looking to create and destroy
        one to one cascading models to showcase
        https://github.com/FactoryBoy/factory_boy/issues/350
        """
        design = factories.DesignFactory()
        initial = 9.5
        design.set_thickness(initial)
        result = design.get_thickness()

        self.assertEqual(initial, result)

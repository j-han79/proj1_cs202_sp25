import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        self.rect = GlobeRect(10.0, 20.0, 30.0, 40.0)
        self.region = Region(self.rect, "Testie", "other")
        self.rc = RegionCondition (self.region, 2025, 1000, 5000.0)
        self.rect2 = GlobeRect(0.0, 10.0, 0.0, 10.0)
        self.region2 = Region(self.rect2, "Biggie", "ocean")
        self.rc2 = RegionCondition(self.region2, 2019, 500000, 1000.0)
        self.zero_pop_rc = RegionCondition(self.region, 2010, 0, 5000.0)

    def test_data_classes_exist(self):
        self.assertIsInstance(self.rect, GlobeRect)
        self.assertIsInstance(self.region, Region)
        self.assertIsInstance(self.rc, RegionCondition)

    def test_emissions_per_capita(self):
        actual = emissions_per_capita(self.rc)
        expected = 5.0
        self.assertAlmostEqual(actual, expected, places = 4)

    def test_emissions_per_capita_zero(self):
        actual = emissions_per_capita(self.zero_pop_rc)
        expected = 0.0
        self.assertAlmostEqual(actual, expected, places = 4)

    def test_area(self):
        actual = area(self.rect)
        self.assertIsInstance(actual, float)
        self.assertGreater(actual, 0.0)

    def test_emissions_per_square_km(self):
        actual = emissions_per_square_km(self.rc)
        expected = self.rc.ghg_rate / area(self.rc.region.rect)
        self.assertAlmostEqual(actual, expected, places = 4)

    def test_densest_single(self):
        actual = densest([self.rc])
        expected = "Testie"
        self.assertEqual(actual, expected)

    def test_densest_multiple(self):
        actual = densest([self.rc, self.rc2])
        expected = "Biggie"
        self.assertEqual(actual, expected)

    def test_project_condition(self):
        projected = project_condition(self.rc, 5)
        self.assertIsInstance(projected, RegionCondition)
        self.assertEqual(projected.year, 2030)
        self.assertEqual(projected.region, self.rc.region)


if __name__ == '__main__':
    unittest.main()

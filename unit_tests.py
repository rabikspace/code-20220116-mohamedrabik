# -*- coding: utf-8 -*-
"""
Unit Test cases for BMI Calculation
"""

import unittest
import bmi_calculation as bmi

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(bmi.bmi_kg_per_m2(96,171), 32.83, "Should be 32.83 kg/m^2")

    def test_case2(self):
        self.assertEqual(bmi.bmi_category(29.7), 'Overweight', "Should be 'Overweight'")
        
    def test_case3(self):
        self.assertEqual(bmi.health_risk('Overweight'), 'Enhanced risk', "Should be 'Enhanced risk'")

if __name__ == '__main__':
    unittest.main()
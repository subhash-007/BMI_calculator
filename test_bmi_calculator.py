import unittest
import bmi_calculator

class TestBmi(unittest.TestCase):
    def test_bmi_calculator(self):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 166, "WeightKg": 62 },
        { "Gender": "Male", "HeightCm": 167, "WeightKg": 82 },
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 162, "WeightKg": 40},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        result = bmi_calculator.bmi_calculator(data)
        self.assertEqual(result[0],2)

if __name__ == "__main__":
    unittest.main


import unittest
import pandas as pd
from main import products, validate_data

import subprocess
import sys

class TestInventoryDataAnalyzer(unittest.TestCase):

# Test 1: Check valid inventory data
    def test_valid_data(self):
        df = pd.DataFrame(products)

        validation_results = validate_data(df)

        self.assertTrue(all(validation_results.values()))


# Test 2: Check duplicate ProductID

    def test_duplicate_product_id(self):
        df = pd.DataFrame(products)
        df.loc[1, "ProductID"] = 101

        validation_results = validate_data(df)
        self.assertFalse(validation_results["Test 1"])


# Test 3: Check negative Price

    def test_negative_price(self):
        df = pd.DataFrame(products)
        df.loc[0, "Price"] = -500

        validation_results = validate_data(df)
        self.assertFalse(validation_results["Test 2"])


# Test 4: Check negative Quantity

    def test_negative_quantity(self):
        df = pd.DataFrame(products)
        df.loc[0, "Quantity"] = -5

        validation_results = validate_data(df)
        self.assertFalse(validation_results["Test 3"])


# Test 5: Check missing values

    def test_missing_values(self):
        df = pd.DataFrame(products)
        df.loc[0, "ProductName"] = None

        validation_results = validate_data(df)
        self.assertFalse(validation_results["Test 4"])


# Test 6: Check all validation conditions

    def test_all_validation_conditions(self):
        df = pd.DataFrame(products)

        validation_results = validate_data(df)

        self.assertEqual(len(validation_results), 4)
        self.assertTrue(validation_results["Test 1"])
        self.assertTrue(validation_results["Test 2"])
        self.assertTrue(validation_results["Test 3"])
        self.assertTrue(validation_results["Test 4"])


# Test 7: Check that importing main.py does not run the program

    def test_import_main(self):
        result = subprocess.run(
            [sys.executable, "-c", "import main"],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

if __name__ == "__main__":
    unittest.main()
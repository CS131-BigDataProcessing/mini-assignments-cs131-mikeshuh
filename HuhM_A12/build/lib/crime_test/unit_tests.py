import unittest
import pandas as pd
import numpy as np
from validate_functions import validate_victim_sex, validate_victim_age
from stats_function import age_mean, age_median

class CrimeDataFrameUnitTests(unittest.TestCase):

    def setUp(self):
        self.valid_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M', 'F', 'M', 'F'],
            'Vict Age': [18, 19, 20, 21, 22, 23]
        })
        self.invalid_df = pd.DataFrame({
            'Vict Sex': ['?', 'F', 'M', 'F', 'M', 'F'],
            'Vict Age': [0, 19, 20, 21, 22, 100]
        })
        self.null_val_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M', 'F', 'M', 'F', None],
            'Vict Age': [18, 19, 20, 21, 22, 23, None]
        })

    def test_validate_victim_sex(self):
        self.assertTrue(validate_victim_sex(self.valid_df))
        self.assertFalse(validate_victim_sex(self.invalid_df))
        self.assertFalse(validate_victim_sex(self.null_val_df))
    
    def test_validate_victim_age(self):
        self.assertTrue(validate_victim_age(self.valid_df))
        self.assertFalse(validate_victim_age(self.invalid_df))
        self.assertFalse(validate_victim_age(self.null_val_df))
    
    def test_age_mean(self):
        self.assertEqual(age_mean(self.valid_df), 20.5)
        self.assertEqual(age_mean(self.invalid_df), np.float64(30.333333333333332))
        self.assertEqual(age_mean(self.null_val_df), 20.5)

    def test_age_median(self):
        self.assertEqual(age_median(self.valid_df), 20.5)
        self.assertEqual(age_median(self.invalid_df), 20.5)
        self.assertEqual(age_median(self.null_val_df), 20.5)

if __name__ == "__main__":
    unittest.main()
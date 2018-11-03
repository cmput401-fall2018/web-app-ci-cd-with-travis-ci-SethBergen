import unittest
from unittest.mock import patch
import service


class TestService(unittest.TestCase):

    @patch("service.Service.bad_random", return_value=6)
    def test_bad_random(self, x):
        """Tests service.Service.bad_random()"""
        result = service.Service().bad_random()
        self.assertEqual(result, 6)

    @patch("service.Service.bad_random", return_value=6)
    def test_divide(self, x):
        """Tests service.Service.divide(y)"""
        result = service.Service().divide(2)
        self.assertEqual(result, 3)

        result = service.Service().divide(-1)
        self.assertEqual(result, -6)

        try:
            result = service.Service().divide(0)
        except ZeroDivisionError:
            result = "ZeroDivisionError"
        self.assertEqual(result, "ZeroDivisionError")
        
    def test_abs_plus(self):
        """Tests service.Service.abs_plus(x)"""
        result = service.Service().abs_plus(1)
        self.assertEqual(result, 2)
        
        result = service.Service().abs_plus(-1)
        self.assertEqual(result, 2)
   
        result = service.Service().abs_plus(0)
        self.assertEqual(result, 1)
        
        result = service.Service().abs_plus(-3.6)
        self.assertEqual(result, 4.6)
        
    @patch("service.Service.bad_random", return_value=6)
    def test_complicated_function(self, x):
        """Tests service.Service.complicated_function(x)"""
        results = service.Service().complicated_function(2)
        self.assertEqual(results[0], 3)
        self.assertEqual(results[1], 0)
        
        
if __name__ == "__main__":
    unittest.main()

import unittest
import service

class TestService(unittest.TestCase):

    @unittest.mock.patch("service.Service.bad_random()", return_value=6)
    def test_bad_random(self):
        result = service.bad_random()
        assertEqual(result, 6)

    @unittest.mock.patch("service.Service.divide()", return_value=6)
    def test_divide(self):
        result = service.divide(2)
        assertEqual(result, 3)
        
    def test_abs_plus(self):
        result = service.abs_plus(1)
        assertEqual(result, 2)
        
        result = service.abs_plus(-1)
        assertEqual(result, 2)
   
       result = service.abs_plus(0)
        assertEqual(result, 1)
        
        result = service.abs_plus(-3.6)
        assertEqual(result, 4.6)
        
    @unittest.mock.patch("service.Service.bad_random()", return_value=6)
    def test_complicated_function():
        results = service.complicated_function(2)
        assertEqual(results[0], 3)
        assertEqual(results[1], 0)
        
        
if __name__ == "__main__":
    unittest.main()

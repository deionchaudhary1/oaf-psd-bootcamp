'''
This function tests the weatherApp's class functionality
'''

import unittest
from a4_APIweatherApp import MockService
from a4_APIweatherApp import APIService
from a4_APIweatherApp import ServiceFactory

class TryTesting(unittest.TestCase):
    def test_create_mock(self):
        mocky = ServiceFactory()
        mock = mocky.create_service(0)
        # Assert that mockFactory creates a mockService object
        self.assertIsInstance(mock, MockService)
    
    def test_create_api(self):
        apiy = ServiceFactory()
        api = apiy.create_service(1)
        # Assert that APIFactory creates a APIService object
        self.assertIsInstance(api, APIService)
        

if __name__ == "__main__":
    unittest.main()
# test_urlvalidator.py
"""
Tests for UrlValidator module.
"""

import unittest
from urlvalidator import UrlValidator

class TestUrlValidator(unittest.TestCase):
    """Test cases for UrlValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UrlValidator()
        self.assertIsInstance(instance, UrlValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UrlValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

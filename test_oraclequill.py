# test_oraclequill.py
"""
Tests for OracleQuill module.
"""

import unittest
from oraclequill import OracleQuill

class TestOracleQuill(unittest.TestCase):
    """Test cases for OracleQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleQuill()
        self.assertIsInstance(instance, OracleQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

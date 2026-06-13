# test_blocklite.py
"""
Tests for BlockLite module.
"""

import unittest
from blocklite import BlockLite

class TestBlockLite(unittest.TestCase):
    """Test cases for BlockLite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockLite()
        self.assertIsInstance(instance, BlockLite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockLite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

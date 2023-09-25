"""
    Name: Christian Del Rosario
    Course/Section: CPE 028 - CPE41S2
    Date: September 25, 2023
    Activity Programming 4.1 - Python Test
"""

import unittest

def greater(num):
    return num >= 100

class TestGreater(unittest.TestCase):

    def test(self):
        self.assertTrue(greater(59))

if __name__ == '__main__':
    unittest.main()
"""
    Name: Christian Del Rosario
    Course/Section: CPE 028 - CPE41S2
    Date: September 25, 2023
    Activity Programming 4.1 - Python Test
"""

import math

def test_greaterOrEqual100():
    num = 100
    assert (num >= 100) is True

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert 7*7 == 49


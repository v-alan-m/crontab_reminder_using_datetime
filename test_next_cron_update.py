'''
Unit test for next_cron_update.py
Terminal command to run (in current directory): 
    python -m unittest test_next_cron_update.py
'''

from next_cron_update import *
import sys
import datetime as dt
from croniter import croniter
import select
import unittest
import os

# Test whether if only the correct number of command lines arguments will be accepted
class Test_argv_input(unittest.TestCase):
    def test_number_of_argv(self):   
        self.assertEqual(argv_num_check(1),None)
        self.assertEqual(argv_num_check(2),True)
        for i in range(3,9):
            self.assertEqual(argv_num_check(i),None)

# Check the time input format, and if the format can not be used then display an error message
class Test_time_format(unittest.TestCase):
    def test_time_format(self):
        # Tests to seeif the correct number of comman lines arguments are given
        self.assertRaises(ValueError, datetime_format, "12:2#")
        self.assertRaises(ValueError, datetime_format, "12:222")
        self.assertRaises(ValueError, datetime_format, "12:AA")
        self.assertRaises(ValueError, datetime_format, "AA:12")
        self.assertRaises(ValueError, datetime_format, "BB:CC")
        self.assertRaises(ValueError, datetime_format, "four:ten")
        self.assertRaises(ValueError, datetime_format, "27:00")
        self.assertRaises(ValueError, datetime_format, "03:63")
__author__ = 'reiscracker'
from unittest import TestCase

from modulescrape.regexhelp import *


class TestRegexHelper(TestCase):

    def setUp( self ):
        super( ).setUp( )
        self.twoColumnRegex = TwoColumnTableRegex()
        self.error_format = "\nError:\n Expected: {}\n Actual: {}".format

    def test_is_column_blank(self):
        # Test if the regex successfully identifies strings where the left or right column (following the pattern) is blank
        sampleRow = "This is a                      beautiful row"
        self.assertFalse(self.twoColumnRegex.is_column_blank(sampleRow))

        sampleRow = "This is a                      "
        self.assertTrue(self.twoColumnRegex.is_column_blank(sampleRow))

        sampleRow = "                     beautiful row"
        self.assertTrue(self.twoColumnRegex.is_column_blank(sampleRow))

        sampleRow = "                     "
        self.assertTrue(self.twoColumnRegex.is_column_blank(sampleRow))

    def test_get_columns(self):
        # Test that the information is correctly returned in their columns
        sampleRow = "This is a                      beautiful row"
        expected = { "left" : "This is a", "right" : "beautiful row" }
        actual = self.twoColumnRegex.get_columns(sampleRow)
        self.assertDictEqual(actual, expected, msg=self.error_format(expected, actual))

        sampleRow = "                      beautiful row"
        expected = { "left" : "", "right" : "beautiful row" }
        actual = self.twoColumnRegex.get_columns(sampleRow)
        self.assertDictEqual(actual, expected, msg=self.error_format(expected, actual))

        sampleRow = "This is a                      "
        expected = { "left" : "This is a", "right" : "" }
        actual = self.twoColumnRegex.get_columns(sampleRow)
        self.assertDictEqual(actual, expected, msg=self.error_format(expected, actual))

        sampleRow = "                       "
        expected = { "left" : "", "right" : "" }
        actual = self.twoColumnRegex.get_columns(sampleRow)
        self.assertDictEqual(actual, expected, msg=self.error_format(expected, actual))


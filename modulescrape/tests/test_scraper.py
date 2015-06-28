__author__ = 'reiscracker'
from unittest import TestCase
from modulescrape import scraper

class TestScraper(TestCase):

    def setUp( self ):
        super( ).setUp( )
        with open('test_handbook.txt') as testFile:
            self.testFileContent = testFile.readlines()

    def test_as_pairs(self):
        myList = [ 1, 2, 3, 4, 5 ]
        expected = [ (1,2), (2,3), (3, 4), (4,5) ]
        actual = list(scraper._as_pairs(myList))
        self.assertListEqual(actual, expected)

    def test_split_modules(self):
        splitted_modules = scraper._split_modules(self.testFileContent)

        # Tests that the right amount of modules was extracted from the text
        expectedModuleCount = 5
        actualModuleCount = len(splitted_modules)
        self.assertEqual(actualModuleCount, expectedModuleCount, msg="5 modules should have been extracted but were not.")
        # Test that the last module (for example) contains the right module name
        expectedLastModuleName = "B15 Gesellschaftliche Aspekte der Informatik"
        actualLastModuleTitle = splitted_modules[-1][0]
        self.assertTrue(expectedLastModuleName in actualLastModuleTitle,
            msg="First line of last extracted module did not contain name %s" % expectedLastModuleName)
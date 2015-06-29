__author__ = 'reiscracker'
# coding: utf-8
import re

class TwoColumnTableRegex():
    """
    Helper class that provides some functions to match and extract data from a two column table text layout
    """
    # A regular expression that will exactly match a two column text table layout.
    # Erster Versuch: twoColumnRegex = '^(.+\w)\s{3,}(\w[\w\s\.]*$)'
    # Zweiter Versuch: twoColumnRegex = '^(\w.*\w)\s{3,}(\w.*\w)'
    # Dritter Versuch: twoColumnRegex = '^(\S+)\s{3,}(\S.*)'
    # Vierter Versuch (grrr): twoColumnRegex = '^(\S.*\S)\s{3,}(\S.*)'
    twoColumnRegex = '^(\S+.*\S*)\s{3,}(\S+.*)' # Yay

    def __init__(self):
        self.pattern = re.compile(self.twoColumnRegex)

    def is_column_blank(self, line):
        """
        Test if one of the columns is blank (e.g. the row is a continuation of the previous row)
        :param line: Line to test
        :return: True if one of the columns contains no value
        """
        return self.pattern.match(line) == None

    def get_columns(self, line):
        """
        Separates both columns of that line
        :param line: The line to separate
        :return: Both columns as a tuple (left, right). If one column contains no value, it is still
            returned as an empty string, e.g. ("", "rightColumnValue")
        """
        leftColumn = rightColumn = ""

        # If both columns contain values, we can just easily split the row using our pattern
        if not self.is_column_blank(line):
            matches = self.pattern.match(line).groups()
            leftColumn, rightColumn = matches[0].strip(), matches[1].strip()

        # If they are not, we need to determine which column has a value and which one doesn't. If the row starts
        # with a character instead of whitespace (pattern match is NOT None == it did match the string), we know that the
        # left column does have content in it (and the content is just the row with leading and trailing whitespaces removed)
        else:
            if re.match('^\S', line) != None:
                leftColumn, rightColumn = line, ""
            else:
                leftColumn, rightColumn = "", line

        # Return the two columns stripped from leading/trailing whitespaces as a dictionary
        return { "left" : leftColumn.strip(), "right" : rightColumn.strip() }


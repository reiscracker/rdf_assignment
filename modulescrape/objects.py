__author__ = 'reiscracker'

class Module:
    """
    Represents a module with its' descriptions and units
    """

    attributeKeys = [
        'Modulname', 'Modulverantwortliche/r', 'Dozent/Dozentin', 'Semesterzugehörigkeit', 'Dauer',
        'Status des Moduls', 'Häufigkeit des Angebotes', 'ECTS-Punkte (Leistungspunkte)', 'Gesamtworkload (für Modul)',
        'Präsenzzeit des Moduls in SWS', 'Prüfungsform / Art der Prüfungsleistung', 'Prüfungsbewertung','Niveaustufe',
        'Lernergebnis / Kompetenzen', 'Notwendige Voraussetzungen', 'Empfohlene Voraussetzungen', 'zugeordnete Units',
        'Verwendbarkeit des Moduls', 'Anerkannte Module', 'Hinweise',
    ]

    @classmethod
    def FromModulePage(cls):
        # Find the end of the module description (the first part) and slice it
        # A completely blank (or empty?) line usually denotes the end of a section, so the first blank line should
        # be the end of the module description

        firstBlankLine = self._find_empty_lines(self.modulePage)[0]
        self.moduleDescription = self.modulePage[:firstBlankLine]
        self._read_attributes_from_table(self.moduleDescription)

    def __init__(self, modulePage):
        """
        Creates a module object from the two pages that describe a module and its' units.
        :param modulePage: Two pages about module and unit description
        """
        self.attributes = {}

    def _read_overall_description(self):
        pass

    def _read_attributes_from_table(self, tableLines):
        """
        Reads a description (module or unit, depending on self.attributeKeys variable) and adds all attributes from that description to this object
        :param tableLines: List of lines containing the table in text format
        :return: Dictionary of attributes read from the table

        # Think this regex is not needed, but took some minutes to write it
        # splitLineRegex = re.compile('^(.+)\s{3,}([\w\s]+)$')

        # Define a function with a regular expression that will return True if the string contains to characters
        # isBlankLine = lambda line: re.search('[^\s]', line) == None
        """
        from modulescrape.regexhelp import TwoColumnTableRegex

        # Helper object providing functions to extract data from a two column table layout
        tableRegex = TwoColumnTableRegex()

        # Accumulator is used to concatenate two subsequent lines if they belong to one attribute.
        leftAcc = rightAcc = ""
        # Now find rows, where both columns have characters, because that's where a new attribute starts
        attributeBeginnings = {}
        for i, row in enumerate(tableLines):
            # First, add the current row to the accumulated lines
            columns = tableRegex.get_columns(row)
            leftAcc += " %s" % columns['left']
            rightAcc += " %s" % columns['right']
            print("Left acc is now: %s \nRight acc is now: %s" % (leftAcc, rightAcc))

            # Now test, if the accumulated lines of the left column build a keyword for an attribute, If so, note
            # the current row as attribute beginning (strip() to remove unwanted whitespaces)
            # if not tableRegex.isColumnBlank(row) and leftAcc.strip() in self.attributeKeys:
            if leftAcc.strip() in self.attributeKeys:
                # attributeBeginnings.append(i)
                attributeBeginnings[leftAcc] = rightAcc
                leftAcc = rightAcc = ""


        print("Attributes begin at rows: ")
        print("%i attributes" % len(attributeBeginnings))
        for a,b in attributeBeginnings.items():
            print("%s\t-->\t%s" % (a,b))
        # return  attributeBeginnings

    def _find_empty_lines(self, lines):
        """
        Returns the indices of empty or whitespace strings in a list of strings
        :param lines: A list of strings
        :return: A list of indices where the list contains empty or whitespace strings as elements
        """
        return [ index for index, line in enumerate(lines) if (not line) or (line.isspace())]

    def __str__(self):
        return "".join(self.moduleDescription)



__author__ = 'reiscracker'
# coding: utf-8

class Module(object):
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

    def __init__(self, modulePage=None):
        """
        Creates a module object from the two pages that describe a module and its' units.
        :param modulePage: Two pages about module and unit description
        """
        from modulescrape.regexhelp import TwoColumnTableRegex
        # Helper object providing functions to extract data from a two column table layout
        self.tableRegex = TwoColumnTableRegex()
        self.attributes = {}
        # Now load information from a module page if one was provided
        if modulePage:
            self.loadFromModulePage(modulePage)


    def loadFromModulePage(self, modulePage):
        """
        Loads information about this module and its' units from those two pages in the pdf that describe one course
        :param modulePage: List of lines representing module + unit description
        """
        moduleTextTable, unitTextTable = self._split_module_unit_descriptions(modulePage)
        self.attributes = self._read_attributes_from_table(moduleTextTable)
        self.attributes["Units"] = [ Unit(t) for t in unitTextTable ]

    def _find_empty_lines(self, lines):
        """
        Returns the indices of empty or whitespace strings in a list of strings
        :param lines: A list of strings
        :return: A list of indices where the list contains empty or whitespace strings as elements
        """
        return [ index for index, line in enumerate(lines) if (not line) or (line.isspace())]

    def _split_module_unit_descriptions(self, modulePage):
        # Find the end of the module description (the first part) and slice it
        # A completely blank (or empty?) line usually denotes the end of a section, so the first blank line should
        # be the end of the module description
        moduleDescriptionEnd = self._find_empty_lines(modulePage)[0]
        moduleDescription, modulePage = modulePage[:moduleDescriptionEnd], modulePage[moduleDescriptionEnd + 1:]

        # Now find the first line with the substring "Name der Unit" as that is where the first unit begins
        unitDescriptionStarts = [ i for i, line in enumerate(modulePage) if line.startswith("Name der Unit") ]
        unitDescriptions = []
        for unitStart in unitDescriptionStarts:
            # First, cut everything until the beginning of the unit
            unitDescription = modulePage[unitStart:]
            # Find the end of the unit by looking for the first empty line, starting from the first line of the unit
            unitEnd = self._find_empty_lines(unitDescription)[0]
            unitDescriptions.append(unitDescription[:unitEnd])
        return (moduleDescription, unitDescriptions)

    def _read_attributes_from_table(self, tableLines):
        """
        Reads a description (module or unit, depending on self.attributeKeys variable) and adds all attributes from that description to this object
        :param tableLines: List of lines containing the table in text format
        :return: Dictionary of attributes read from the table
        """
        # Accumulator is used to concatenate two subsequent lines if they belong to one attribute.
        leftAcc = rightAcc = ""
        tableRowCount = len(tableLines)
        # Now find rows, where both columns have characters, because that's where a new attribute starts
        attributes = {}
        for i, row in enumerate(tableLines):
            # First, add the current row to the accumulated lines
            columns = self.tableRegex.get_columns(row)
            leftAcc += "%s " % columns['left']
            rightAcc += "%s " % columns['right']
            print("Left acc is now: %s \nRight acc is now: %s" % (leftAcc, rightAcc))

            # Now test, if the accumulated lines of the left column build a keyword for an attribute, If so, we still have
            # to check, whether the next row is a continuation of the current row (means a blank row in either column)
            # If it's not, because a new row begins, and no column is empty, save the currently accumulated attribute
            # to out list (after stripping whitespaces)
            print("i is at %s" % i)
            if leftAcc.strip() in self.attributeKeys:
                # We did accumulate an attribute key! But we have to check, if the next row might be a continuation of our current one
                # Also, we may not run too far with our index. If we do, just write the last line and exit
                if i >= tableRowCount - 1:
                    attributes[leftAcc.strip()] = rightAcc.strip()
                    break
                # If we can, check for row continuation. Only write when the next row starts a new attribute
                if not self.tableRegex.is_column_blank(tableLines[i+1]):
                    attributes[leftAcc.strip()] = rightAcc.strip()
                    leftAcc = rightAcc = ""

        print("%s attributes read" % len(attributes))
        return  attributes

    def __str__(self):
        # Keep 10 characters to the left terminal border
        marginLeft = "{:>5}".format(" ")
        heading = "{:>3}MODUL:\n".format(" ")
        lineFormat = (marginLeft + "{:<50}\t-->\t{:<50}").format
        s = heading + "\n".join([ lineFormat(k,v) for (k,v) in self.attributes.iteritems() ])
        return s

class Unit(Module):

    attributeKeys = [
        "Name der Unit", "Name des zugeordneten Moduls", "Sprache", "Anteil Workload für die Unit", "Anteil Präsenzzeit in SWS",
        "Lernform", "Inhalt der Unit", "Literatur", "Hinweise"
    ]

    def __init__(self, unitTextTable):
        super(Unit, self).__init__()
        self.textTable = unitTextTable
        self.attributes = self._read_attributes_from_table(self.textTable)

    def __repr__( self ):
        # lineFormat = "\t\t\t{:<30}\t-->\t{:<30}".format
        # s = "\n".join([ lineFormat(k,v) for (k,v) in self.attributes.iteritems() ])
        # return s
        return self.__str__()

    def __str__( self ):
        marginLeft = "{:>10}".format(" ")
        heading = "\n{:>8}UNIT:\n".format(" ")
        lineFormat = (marginLeft + "{:<55}\t-->\t{:<55}").format

        s = heading + "\n".join([ lineFormat(k,v) for (k,v) in self.attributes.iteritems() ])
        return s


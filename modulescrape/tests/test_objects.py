__author__ = 'reiscracker'
# coding: utf-8

from unittest import TestCase
from output import style as Style
from modulescrape import objects

class TestObjects(TestCase):

    def setUp( self ):
        super(TestObjects, self).setUp()
        self.module = objects.Module()
        with open('modulepage.txt') as testFile:
            self.modulePage = testFile.readlines()

    def test_find_empty_lines(self):
        # Test that the function returns the indices of all empty of whitespace lines
        listWithBlankLines = [
            "   ",
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam",
            "",
            "et ea rebum. Stet clita kasd gubergren, no s",
            "                   ",
            "ea takimata sanctus est Lorem ipsum",
            "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed",
            "d",
            "agna aliquyam erat, sed",
            ",",
            "           ",
            "kasd gubergren, no sea takimata sanctus est Lo",
            "rem ipsum dolor sit amet",
            ""
        ]
        expected = [
            0, 2, 4, 10, 13
        ]
        actual = self.module._find_empty_lines(listWithBlankLines)
        self.assertListEqual(actual, expected, msg=Style.test_error_format(expected, actual))

    def test_split_module_unit_description(self):
        expectedModuleDescription = [
            "Modulname                   B21 Algorithmen und Datenstrukturen\n",
            "Modulverantwortliche/r      Prof. Dr., Jürgen Sieck\n",
            "Dozent/Dozentin             Prof. Dr., Jürgen Sieck, Prof. Dr. Frank Bauernöppel\n",
            "Semesterzugehörigkeit       2. Semester\n",
            "Dauer                       ein Semester\n",
            "Status des Moduls           Pflichtmodul\n",
            "Häufigkeit des              in jedem Semester\n",
            "Angebotes\n",
            "ECTS-Punkte                 5\n",
            "(Leistungspunkte)\n",
            "Gesamtworkload              150 Stunden\n",
            "(für Modul)\n",
            "Präsenzzeit des Moduls      3 SWS\n",
            "in SWS\n",
            "Prüfungsform / Art der      Modulprüfung gemäß §§14-16 RPO der HTW Berlin bzw.\n",
            "Prüfungsleistung            modulbegleitend geprüfte Studienleistungen gemäß §17 RPO der\n",
            "                            HTW Berlin\n",
            "Prüfungsbewertung           Differenziert nach Noten\n",
            "Niveaustufe                 1b (voraussetzungsbehaftetes Modul, in Bachelorstudiengängen)\n",
            "Lernergebnis /               Die Studierenden kennen wichtige Algorithmen und die\n",
            "Kompetenzen                     zugehörigen Datenstrukturen\n",
            "                             Sie können für grundlegende Aufgabenstellungen passende\n",
            "                                Algorithmen und Datenstrukturen auswählen\n",
            "                             Die Studierenden können die Laufzeit von Algorithmen\n",
            "                                bewerten, vergleichen und in die zugehörigen\n",
            "                                Komplexitätsklassen einordnen\n",
            "                             Sie erwerben Fachkompetenz zu Analyse und Design von\n",
            "                                Algorithmen\n",
            "Notwendige                  Keine\n",
            "Voraussetzungen\n",
            "Empfohlene                  B11: Theoretische Grundlagen der Informatik,\n",
            "Voraussetzungen             B13: Programmierung 1\n",
            "zugeordnete Units            B21.1 Algorithmen und Datenstrukturen (SL)\n",
            "                             B21.2 Algorithmen und Datenstrukturen (Ü)\n",
            "Verwendbarkeit des          Keine\n",
            "Moduls\n",
            "Anerkannte Module           Keine\n",
            "Hinweise                    Medienformen:\n",
            "                            Folien-Präsentationen über Beamer, Programmdemonstrationen,\n",
            "                            Tafelanschrieb, Laborübungen am Rechner\n",
        ]
        expectedUnitDescriptions = [
            [
                "Name der Unit            B21.1 Algorithmen und Datenstrukturen (SL)\n",
                "Name des                 B21 Algorithmen und Datenstrukturen\n",
                "zugeordneten Moduls\n",
                "Sprache                  Deutsch\n",
                "Anteil Workload für      50%\n",
                "die Unit\n",
                "Anteil Präsenzzeit in    2 SWS\n",
                "SWS\n",
                "Lernform                 Seminaristischer Lehrvortrag\n",
                "Inhalt der Unit           grundlegende Datenstrukturen (Stacks, Queues, div.\n",
                "                            Baumstrukturen)\n",
                "                          Sortier- und Suchverfahren, Graphalgorithmen,\n",
                "                            Hashverfahren, mathematische Algorithmen\n",
                "                          Algortihmische Prinzipien wie Teile-und-Herrsche,\n",
                "                            Bachtracking, Rekursion, Depth-first-search\n",
                "                          Kryptografie (Caesar, einache Public-Key Verfahren)\n",
                "                          Datenkompression (Lauflängenkod., Huffmann)\n",
                "                          O-Noation, Komplexitätsabschätzungen\n",
                "Literatur                 Sedgewick, „Algorithmen“, Addison-Wesley\n",
                '                          "Algorithmen und Datenstrukturen - Eine Einführung mit\n',
                '                            JAVA"; G. Saake, K.U. Sattler; dpunkt Verlag\n',
                '                          weitere Literatur wird vom Dozenten festgelegt\n',
                'Hinweise\n',
            ],
            [
                'Name der Unit            B21.2 Algorithmen und Datenstrukturen (Ü)\n',
                'Name des                 B21 Algorithmen und Datenstrukturen\n',
                'zugeordneten Moduls\n',
                'Sprache                  Deutsch\n',
                'Anteil Workload für      50%\n',
                'die Unit\n',
                'Anteil Präsenzzeit in    1 SWS\n',
                'SWS\n',
                'Lernform                 Laborübung\n',
                'Inhalt der Unit           grundlegende Datenstrukturen (Stacks, Queues, div.\n',
                '                            Baumstrukturen)\n',
                '                          Sortier- und Suchverfahren, Graphalgorithmen,\n',
                '                            Hashverfahren, mathematische Algorithmen\n',
                '                          Algortihmische Prinzipien wie Teile-und-Herrsche,\n',
                '                            Bachtracking, Rekursion, Depth-first-search,\n',
                '                          Kryptografie (Caesar, einache Public-Key Verfahren)\n',
                '                          Datenkompression (Lauflängenkod., Huffmann)\n',
                '                          O-Noation, Komplexitätsabschätzungen\n',
                'Literatur                 Sedgewick, „Algorithmen“, Addison-Wesley\n',
                '                          "Algorithmen und Datenstrukturen - Eine Einführung mit\n',
                '                            JAVA"; G. Saake, K.U. Sattler; dpunkt Verlag\n',
                '                          weitere Literatur wird vom Dozenten festgelegt\n',
                'Hinweise\n',
            ]
        ]
        actualModuleDescription, actualUnitDescriptions = self.module._split_module_unit_descriptions(self.modulePage)
        self.assertListEqual(actualModuleDescription, expectedModuleDescription, msg=Style.print_with_metacharacters(expectedModuleDescription, actualModuleDescription))
        self.assertListEqual(actualUnitDescriptions[0], expectedUnitDescriptions[0], msg=Style.print_with_metacharacters(expectedUnitDescriptions[0], actualUnitDescriptions[0]))
        self.assertListEqual(actualUnitDescriptions[1], expectedUnitDescriptions[1], msg=Style.print_with_metacharacters(expectedUnitDescriptions[1], actualUnitDescriptions[1]))

    def test_read_attributes_from_table(self):
        attributeTable = [
            "Modulname                   B21 Algorithmen und Datenstrukturen",
            "Modulverantwortliche/r      Prof. Dr., Jürgen Sieck",
            "Dozent/Dozentin             Prof. Dr., Jürgen Sieck, Prof. Dr. Frank Bauernöppel",
            "Semesterzugehörigkeit       2. Semester",
            "Dauer                       ein Semester",
            "Status des Moduls           Pflichtmodul",
            "Häufigkeit des              in jedem Semester",
            "Angebotes",
            "ECTS-Punkte                 5",
            "(Leistungspunkte)",
            "Gesamtworkload              150 Stunden",
            "(für Modul)",
            "Präsenzzeit des Moduls      3 SWS",
            "in SWS",
            "Prüfungsform / Art der      Modulprüfung gemäß §§14-16 RPO der HTW Berlin bzw.",
            "Prüfungsleistung            modulbegleitend geprüfte Studienleistungen gemäß §17 RPO der",
            "                            HTW Berlin",
            "Prüfungsbewertung           Differenziert nach Noten",
            "Niveaustufe                 1b (voraussetzungsbehaftetes Modul, in Bachelorstudiengängen)",
            "Lernergebnis /               Die Studierenden kennen wichtige Algorithmen und die",
            "Kompetenzen                     zugehörigen Datenstrukturen",
            "                             Sie können für grundlegende Aufgabenstellungen passende",
            "                                Algorithmen und Datenstrukturen auswählen",
            "                             Die Studierenden können die Laufzeit von Algorithmen",
            "                                bewerten, vergleichen und in die zugehörigen",
            "                                Komplexitätsklassen einordnen",
            "                             Sie erwerben Fachkompetenz zu Analyse und Design von",
            "                                Algorithmen",
            "Notwendige                  Keine",
            "Voraussetzungen",
            "Empfohlene                  B11: Theoretische Grundlagen der Informatik,",
            "Voraussetzungen             B13: Programmierung 1",
            "zugeordnete Units            B21.1 Algorithmen und Datenstrukturen (SL)",
            "                             B21.2 Algorithmen und Datenstrukturen (Ü)",
            "Verwendbarkeit des          Keine",
            "Moduls",
            "Anerkannte Module           Keine",
            "Hinweise                    Medienformen:",
            "                            Folien-Präsentationen über Beamer, Programmdemonstrationen,",
            "                            Tafelanschrieb, Laborübungen am Rechner",
        ]
        expected = {
            "Modulname" : "B21 Algorithmen und Datenstrukturen",
            "Modulverantwortliche/r" : "Prof. Dr., Jürgen Sieck",
            "Dozent/Dozentin" : "Prof. Dr., Jürgen Sieck, Prof. Dr. Frank Bauernöppel",
            "Semesterzugehörigkeit" : "2. Semester",
            "Dauer" : "ein Semester",
            "Status des Moduls" : "Pflichtmodul",
            "Häufigkeit des Angebotes" : "in jedem Semester",
            "ECTS-Punkte (Leistungspunkte)" : "5",
            "Gesamtworkload (für Modul)" : "150 Stunden",
            "Präsenzzeit des Moduls in SWS" : "3 SWS",
            "Prüfungsform / Art der Prüfungsleistung" : "Modulprüfung gemäß §§14-16 RPO der HTW Berlin bzw. modulbegleitend geprüfte Studienleistungen gemäß §17 RPO der HTW Berlin",
            "Prüfungsbewertung" : "Differenziert nach Noten",
            "Niveaustufe" : "1b (voraussetzungsbehaftetes Modul, in Bachelorstudiengängen)",
            "Lernergebnis / Kompetenzen" : " Die Studierenden kennen wichtige Algorithmen und die zugehörigen Datenstrukturen " \
                + " Sie können für grundlegende Aufgabenstellungen passende Algorithmen und Datenstrukturen auswählen " \
                + " Die Studierenden können die Laufzeit von Algorithmen bewerten, vergleichen und in die zugehörigen Komplexitätsklassen einordnen " \
                + " Sie erwerben Fachkompetenz zu Analyse und Design von Algorithmen",
            "Notwendige Voraussetzungen" : "Keine",
            "Empfohlene Voraussetzungen" : "B11: Theoretische Grundlagen der Informatik, B13: Programmierung 1",
            "zugeordnete Units" : " B21.1 Algorithmen und Datenstrukturen (SL)  B21.2 Algorithmen und Datenstrukturen (Ü)",
            "Verwendbarkeit des Moduls" : "Keine",
            "Anerkannte Module" : "Keine",
            "Hinweise" : "Medienformen: Folien-Präsentationen über Beamer, Programmdemonstrationen, " \
                "Tafelanschrieb, Laborübungen am Rechner"
        }
        actual = self.module._read_attributes_from_table(attributeTable)
        self.assertDictEqual(actual, expected, msg=Style.print_with_metacharacters(expected, actual))

        # def test_read_attributes_from_table(self):
        #     expected = {
        #         "Modulname" : "B15 Gesellschaftliche Aspekte der Informatik",
        #         "Modulverantwortliche/r" : "Prof. Dr. Christin Schmidt",
        #         "Dozent/Dozentin" : "Prof. Dr. C. Schmidt / LB RA Harald Keil",
        #         "Semesterzugehörigkeit" : "1. Semester",
        #         "Dauer" : "ein Semester",
        #         "Status des Moduls" : "Pflichtmodul",
        #         "Häufigkeit des Angebotes" : "in jedem Semester",
        #         "ECTS-Punkte (Leistungspunkte)" : "5",
        #         "Gesamtworkload (für Modul)" : "150 Stunden",
        #         "Präsenzzeit des Moduls in SWS" : "4 SWS",
        #         "Prüfungsform / Art der Prüfungsleistung" : "Modulprüfung gemäß §§14-16 RPO der HTW Berlin bzw. modulbegleitend geprüfte Studienleistungen gemäß §17 RPO der HTW Berlin",
        #         "Prüfungsbewertung" : "Differenziert nach Noten",
        #         "Niveaustufe" : "1a (voraussetzungsfreies Modul, in Bachelorstudiengängen)",
        #         "Lernergebnis / Kompetenzen " : "Die Studierenden erwerben  Informatische Fachkompetenz: Praktisch gestalterische Kompetenz - Analyse und Design  " \
        #             + "Fachübergreifende Sachkompetenz: Juristische Grundkompetenz  Methodenkompetenzen • Analytische Kompetenz: Urteils- und Entscheidungskompetenz, wissenschaftliches Arbeiten " \
        #             + "•   Transferkompetenz: Präsentationskompetenz  Sozialkompetenz: Kommunikative Kompetenz  Selbstkompetenz",
        #         "Notwendige Voraussetzungen" : "keine",
        #         "Empfohlene Voraussetzungen" : "keine",
        #         "zugeordnete Units" : "   B15.1 Gesellschaftliche Aspekte der Informatik (SL)",
        #         "Verwendbarkeit des Moduls" : "",
        #         "Anerkannte Module" : "",
        #         "Hinweise" : ""
        #     }
        #     actual = self.module._read_attributes_from_table(self.modulePage)

        # def test_as_pairs(self):
        #     myList = [ 1, 2, 3, 4, 5 ]
        #     expected = [ (1,2), (2,3), (3, 4), (4,5) ]
        #     actual = list(newscraper._as_pairs(myList))
        #     self.assertListEqual(actual, expected)
        #
        # def test_split_modules(self):
        #     splitted_modules = newscraper._split_modules(self.testFileContent)
        #
        #     # Tests that the right amount of modules was extracted from the text
        #     expectedModuleCount = 5
        #     actualModuleCount = len(splitted_modules)
        #     self.assertEqual(actualModuleCount, expectedModuleCount, msg="5 modules should have been extracted but were not.")
        #     # Test that the last module (for example) contains the right module name
        #     expectedLastModuleName = "B15 Gesellschaftliche Aspekte der Informatik"
        #     actualLastModuleTitle = splitted_modules[-1][0]
        #     self.assertTrue(expectedLastModuleName in actualLastModuleTitle,
        #                     msg="First line of last extracted module did not contain name %s" % expectedLastModuleName)

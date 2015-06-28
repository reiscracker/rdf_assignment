__author__ = 'reiscracker'
import os
from modulescrape.objects import Module

def _as_pairs(iterable):
    """
    Returns an iterable object as pairs of two subsequent items
    For example: [ 1, 2, 3, 4 ] -> [ (1, 2), (2, 3), (3, 4) ]
    :param iterable: Something iterable
    :return: List of pairs of subsequent items
    """
    import itertools
    # Create two iterators, both pointing to the first element in the list
    a, b = itertools.tee(iterable)
    # Increase the second iterator by one. Now "a" points to the first element, "b" to the second
    next(b, None)
    # Zip takes both iterators and advances them until the end, but because "b" is always one element
    # ahead of "a", we get the list as pairs
    return zip(a, b)

def _split_modules(module_handbook_text):
    """
    Takes the content of the module handbook and splits it by module pages. A module page contains the overall
    module description and its' unit descriptions
    :param module_handbook_text: content of the handbook file
    :return: list (modules) of lists (the lines of that module)
    """
    # Find the lines where a new module description starts (i = line index, l = line content)
    moduleBeginnings = [ i for i, l in enumerate(module_handbook_text) if l.startswith("Modulname") ]
    # Add last line of the document so the last module (last appearance of "Modulname" until EOF) will be extracted
    moduleBeginnings.append(len(module_handbook_text))

    # Use slicing to extract each module
    modules = []
    for (thisModuleBegin, nextModuleBegin) in _as_pairs(moduleBeginnings):
        print("Slicing from %s to %s" % ( thisModuleBegin, nextModuleBegin ))
        # Slice from the start of a module description until the start of the next module description
        modules.append( module_handbook_text[thisModuleBegin:nextModuleBegin] )

    print("Read %s modules" % len(modules))
    return modules


def read_modules(handbuch_textfile_path):
    """
    Alright this might get messy, let's see
    :param handbuch_textfile_path: PDF modulhandbuch converted into a text file where the layout was preserved
    """
    # File must exist, else we can not continue
    if not (os.path.exists(handbuch_textfile_path) and os.path.isfile(handbuch_textfile_path)):
        raise "%s is either not a file or does not exist" % handbuch_textfile_path

    # Open file and read contents
    with open(handbuch_textfile_path, "r") as file:
        moduleHandbookText = file.readlines()

    # Now split file (handbook) content into pages of separate module descriptions
    splittedModulePages = _split_modules(moduleHandbookText)
    leModule = Module(splittedModulePages[0])


    # modules = []
    # current_module = {}
    # # Read until a new module starts
    #
    #
    # # In the end there will be a list of separate module "pages" (which is a list of strings)
    # splitted_modules = []
    # new_module = []
    #
    # for line in file:
    #     # Whenever there is "Modulname" in the text, a module page starts
    #     if (line.startswith("Modulname")):
    #         splitted_modules.append(new_module)
    #         new_module = []
    #     new_module.append(line)
    # # Strip away the first one as this does not contain a module, but headers etc
    # splitted_modules = splitted_modules[1:]
    # print("Modules found: " + str(len(splitted_modules)))


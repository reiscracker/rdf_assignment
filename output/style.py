__author__ = 'reiscracker'
# coding: utf-8
import collections

def test_error_format(expected, actual):

    format_iterable_comparable = lambda ex, ac: "Expected: \t{}\nActual: \t{}".format(ex.rstrip(), ac.rstrip())
    format_simple = "\nError:\n Expected: {}\n Actual: {}".format

    if isinstance(expected, collections.Iterable) and isinstance(actual, collections.Iterable):
        formatted_string = "\n".join([ format_iterable_comparable(ex, ac) for (ex, ac) in zip(expected, actual) ])
    else:
        formatted_string = format_simple(expected, actual)
    return "MERGED BEGIN\n" + formatted_string

def print_with_metacharacters(expected, actual):
    format_iterable_comparable = lambda ex, ac: "Expect: {}\nActual: {}".format(repr(ex), repr(ac))
    format_simple = repr("Expected: {}\nActual: {}".format)

    if isinstance(expected, collections.Iterable) and isinstance(actual, collections.Iterable):
        formatted_string = "\n".join([ format_iterable_comparable(ex, ac) for (ex, ac) in zip(expected, actual) ])
    else:
        formatted_string = format_simple(expected, actual)
    return "\n" + formatted_string

class TermColors:
    # format_iterable_comparable_colored = lambda ex, ac: (TermColors.OKGREEN + "{}\n" + TermColors.RED + "{}").format(ex.rstrip(), ac.rstrip())
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[0;31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

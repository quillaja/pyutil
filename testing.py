"""
Some simple utiities to help with testing, but not as robust as
the built in python unit testing.
"""


def is_expected(expected_output, actual_output):
    """Compares the expected input and output"""
    return expected_output == actual_output


def print_test(expected_output, actual_output):
    """Compares the input and output and prints the result."""
    is_exp = is_expected(expected_output, actual_output)
    print('%s\tgot %s, expected %s' % (is_exp, actual_output, expected_output))


def perform_tests(func, test_cases):
    """
    Performs a list of test cases on func. The list of test_cases
    should be a list of tupples:
        (<the expected output>, <the input to func>)
    Of course, func must take a single input and produce a single output.
    """
    for t in test_cases:
        print_test(t[0], func(t[1]))

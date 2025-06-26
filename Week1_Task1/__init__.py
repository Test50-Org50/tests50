import check50
import check50.c
import re


@check50.check()
def exists():
    """average.c exists"""
    check50.exists("average.c")


@check50.check(exists)
def compiles():
    """average.c compiles"""
    check50.c.compile("average.c", lcs50=True)


@check50.check(compiles)
def test_example():
    """calculates average correctly for example input (2.5, 3.7, 4.1)"""
    check_average("2.5", "3.43")


@check50.check(compiles)
def test_integers():
    """calculates average correctly for integer inputs (1, 2, 3)"""
    check_average("1", "2.00")


@check50.check(compiles)
def test_decimals():
    """calculates average correctly for decimal inputs (1.5, 2.5, 3.0)"""
    check_average("1.5", "2.33")


@check50.check(compiles)
def test_negative():
    """calculates average correctly with negative numbers (-1.0, 0.0, 1.0) """
    check_average("-1.0", "0.00")


@check50.check(compiles)
def test_large_numbers():
    """calculates average correctly for large numbers (100.5, 200.3, 300.2)"""
    check_average("100.5", "200.33")


def check_average(a, expected_avg):
    """Helper function to check average calculation"""
    # Define expected, actual outputs
    expected = f"Average: {expected_avg}\n"
    actual = check50.run("./average").stdin(a).stdout()

    # Check output
    if not re.match(regex(expected_avg), actual):
        try:
            last_character = actual[-1]
        except IndexError:
            raise check50.Mismatch(expected=expected, actual=actual)

        raise check50.Mismatch(expected=expected, actual=actual)


def regex(avg_value):
    """Create regex pattern for expected output format (newline optional)"""
    return f"^Average: {re.escape(avg_value)}\\n?$"

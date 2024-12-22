from .Tester import Tester

__version__ = "1.0.0"

class TestFail(Exception): pass

def assertEq(val1, val2):
    if val1 != val2: raise TestFail(f"{val1 = } not equal {val2 = }")


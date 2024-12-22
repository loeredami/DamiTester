# Tester
A library for writing simple test functions in python, and getting proper results.

# Usage
```python
# test.py
from Tester import Tester

# Create a tester
tester = Tester()

# Create a test
@tester.test
def hasTest():
  with open("test.txt", "r") as src:
    data = src.read()

tester.run_all_tests()
```

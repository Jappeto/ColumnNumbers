#test_columnNumbers.py
# Jacob Reppeto
# ----------------------------------------------------------------------
import unittest
import columnNumbers

class Test_ColumnNumbers(unittest.TestCase):
    def test_columnNumbers1(self):
        s="""1a2
34b
c56
7d8"""
        self.assertEqual(columnNumbers.columnNumbers(s), [142, 356])

    def test_columnNumbers2(self):
        s="""123
456
789"""
        self.assertEqual(columnNumbers.columnNumbers(s), [123, 456, 789])

    def test_columnNumbers3(self):
        s="""1a
456
891"""
        self.assertEqual(columnNumbers.columnNumbers(s), [156, 491])

    def test_columnNumbers4(self):
        s="""1a2
34
56b
789"""
        self.assertEqual(columnNumbers.columnNumbers(s), [142, 369])
    def test_columnNumbersIfNo3DigitNumber(self):
        s="""abc
def
ghi"""
        self.assertEqual(columnNumbers.columnNumbers(s), "")

    def test_columnNumbersIfNot3DigitNumber2(self):
        s="""12a
34b
56c"""
        self.assertEqual(columnNumbers.columnNumbers(s), "")

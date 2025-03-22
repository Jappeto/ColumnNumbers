#!/usr/bin/env python3

# ----------------------------------------------------------------------
# columnNumbers.py
# Jacob Reppeto
# ----------------------------------------------------------------------

from typing import List


def columnNumbers(s: str) -> List[int]:
    """
    Processes a multiline string where each line starts with digits and extracts the first
    three digits of each line to form 3-digit numbers. The digits are treated as separate
    columns and combined into a single integer for each row up to the smallest number of
    digits present across the columns.

    :param s: A multiline string where each line may start with digits.
    :type s: str
    :return: A list of integers formed by combining the first three digits of each line
        across all the rows.
    :rtype: List[int]
    """
    columns = [[], [], []]
    lines = s.splitlines()


    for line in lines:
        for i in range(len(line)):
            char = line[i]
            if char.isdigit() and i < 3:  # Only consider first three columns
                columns[i].append(char)

    # Find the minimum number of complete rows that can be formed
    minLength = len(columns[0])
    for column in columns:
        if len(column) < minLength:
            minLength = len(column)

    if minLength == 0:
        return ""

    finalResult = []
    for i in range(minLength):
        number = int(columns[0][i] + columns[1][i] + columns[2][i])  # Form numbers correctly
        finalResult.append(number)

    return finalResult


def main():
    s = """1a2
34b
c56
7d8"""
    assert columnNumbers(s) == [142, 356]


# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # First count the number of a's.
    # Then // floor divide with length of s which returns nearest integer.
    # Now count number of a's in rest of the string.
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
# Import collections module for Counter function
import collections

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # Finds number of Occurances of each character in a
    count_a = collections.Counter(a)
    # Finds number of Occurances of each character in b
    count_b = collections.Counter(b)
    # Subtract inorder to remove same alphabet occurances and return remaining characters occurances in a
    c = count_a - count_b
    # Subtract inorder to remove same alphabet occurances and return remaining character occurances in b
    d = count_b - count_a
    # Add both remaining occurances
    e = c + d
    #Get the list of elements to be deleted by using "list()" function and find out the length of the list by "len()" function.
    minimum_deletions = len(list(e.elements()))
    # Return the count of minimum deletions to make an anagram.
    return minimum_deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

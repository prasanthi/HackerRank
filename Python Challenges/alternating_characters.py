#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    minimum_deletions = 0
    # Iterate from 1 to the length of string
    for i in range(1,len(s)):
        # If 2 successive characters are same, delete one of them.
        if(s[i] == s[i-1]):
            minimum_deletions= minimum_deletions+1
    # return the total number of minimum deletions.
    return minimum_deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

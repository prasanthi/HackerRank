#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append("$")
    pairs = 0
    i = 0
    while i<n:
        # check for the same colored pairs
        if ar[i]==ar[i+1]:
            # If matches increment pairs
            pairs = pairs+1
            # To check for next match increment i
            i= i+2
        else:
            # As it is not a match increment i for finding the next match
            i = i+1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

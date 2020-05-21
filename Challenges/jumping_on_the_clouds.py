#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # To count the no of jumps
    jumps = 0
    i = 0
    # condition to run the loop till the end of array
    while (i<len(c)-1):
        # To take a jump check whether if it is the end of array and even for the cumulus
        if (i+2)<len(c) and c[i+2]==0:
            i = i+2
            jumps = jumps+1
        else:
            i = i+1
            jumps = jumps+1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    valley_counter = 0
    for i in range(n):
        # checking for upward step
        if (s[i]=="U"):
            # as it is up step increment the altitude
            altitude = altitude + 1
            # if the altitude is zero means sea level
            if (altitude==0):
                # as it is sea level it means a valley
                valley_counter = valley_counter + 1
        else:
            # if it is down step decrement the altitude
            altitude = altitude - 1
    # Finally return the total no of valleys
    return valley_counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

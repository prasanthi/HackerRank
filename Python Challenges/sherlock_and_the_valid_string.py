
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # Iterate and count how many times string occured
    character_dict = {}
    for character in s:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    #initiate largest and smallest count with last character
    min_count = character_dict[character]
    max_count = character_dict[character]
    # count how many times a count occured
    count_dict = {}
    for char, value in character_dict.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
        #also update max and min count
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value
    # final test:
    if len(count_dict) == 1:
        return "YES"
    elif len(count_dict) == 2:
        if count_dict[max_count] == 1 and max_count - min_count == 1:
            return "YES"
        elif count_dict[min_count] == 1 and min_count == 1:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def backTrack(val, arr, px):
    counter = len(arr) - 1
    diff = 1
    if counter <= 0:
        return 1
    
    print(counter, len(arr))
    while counter >= 0:
        print(counter, px[counter], val)
        if px[counter] > val:
            counter -= arr[counter]
            diff += arr[counter]
        else:
            break
    print(arr, px, diff, val)
    return diff

def maxDifference(px):
    # Write your code here
    diff = []
    maxDiff = -999999999
    for item in px:
        a = backTrack(item, diff, px)
        if a > maxDiff:
            maxDiff = a
        diff.append(a)
    return maxDiff
    

if __name__ == '__main__':
    print(maxDifference([2, 3, 10, 2, 4, 8, 1]))
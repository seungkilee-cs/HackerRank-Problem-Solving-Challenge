'''
2021/10/11 M

https://www.hackerrank.com/challenges/apple-and-orange/problem

overlapping interval problem (inclusive)

m   -> apples
n   -> oranges
s-t -> house width
a   -> left, apple
b   -> right, orange


'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples, appleCount   = map(lambda x: x+a, apples), 0
    oranges, orangeCount = map(lambda x: x+b, oranges), 0
    
    for _idx, applePos in enumerate(apples):
        if applePos >= s and applePos <= t:
            appleCount += 1
    
    for _idx, orangesPos in enumerate(oranges):
        if orangesPos >= s and orangesPos <= t:
            orangeCount += 1
            
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
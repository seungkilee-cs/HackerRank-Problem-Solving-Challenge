'''
2021/10/09 S

Given an integer, , find the smallest integer  such that  is divisible by  (i.e.,  is a factor of ) and satisfies the following properties:

 must not contain zeroes in its decimal representation.
The sum of 's digits must be greater than or equal to the product of 's digits.
Given , find  and print the number of digits in 's decimal representation.

Input Format

A single integer denoting .

Constraints

 is not divisible by .
Time Limits

The time limits for this challenge are available here.
Output Format

Print the number of digits in the decimal representation of the smallest possible .

Sample Input 0

1
Sample Output 0

1
Explanation 0

 is evenly divided by , doesn't contain any zeroes in its decimal representation, and the sum of its digits is not less than the product of its digits. Thus, we print the number of digits in  (which also happens to be ) as our answer.

Sample Input 1

9
Sample Output 1

1
Explanation 1

 is evenly divided by , doesn't contain any zeroes in its decimal representation, and the sum of its digits is not less than the product of its digits. Thus, we print the number of digits in , which is , as our answer.

n is a factor of m -> m/n = int
0 not in str(m) or reduce(lambda x,y : x*y, str(n)) is not 0
reduce(lambda x,y : x+y, int(str(n))) > reduce(lambda x,y : x*y, int(str(n)))

take n and split it to array of ints
m candidate should be multiple of n. -> increment by the loop count. unless that loop contains 0.
check if the sum is greater than the product
-> too slow?
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'divisibleNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumDigits(numList):
    return reduce(lambda x,y: x+y, numList)

def prodDigits(numList):
    return reduce(lambda x,y: x*y, numList)

def divisibleNumbers(n):
    """
    - n is a factor of m -> m is a multiple of n | isinstance(m/n, int)
    - m does not contain 0 -> reduce(lambda x,y: x+y, n[]) is not 0
    - sum of digits > product of digits -> reduce(lambda x,y: x+y, n[]) > reduce(lambda x,y: x*y, n[])
    
    1. Take n and split it to array of digits | max len(n[]) = 5, min len(n[]) = 1 | O(1)
    2. m candidates will always be multiple of n. Loop and increment by n. Check if the product of the digits of m contains 0 | O(1)
    3. If sum is greather than the product, it's our winner. | O(1) + O(1) in O(3x10^4 / n) -> O(n)
    """
    
    m, mList = n, [int(d) for d in str(n)]
    
    while(True): # O(n)
        prod = prodDigits(mList) # O(1~5) -> O(1)
        if(prod):
            if(prod <= sumDigits(mList)):
                return len(str(m))        
        # else
        m += n
        mList = [int(d) for d in str(m)] # O(2n) -> O(n)
    
    return len(mList)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = divisibleNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()

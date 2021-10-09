'''
2021/10/08 F

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

'''
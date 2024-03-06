'''
DataLemur - Factorial Problem 
Given a number nn, write a formula that returns n!n!.

In case you forgot the factorial formula, n!=n∗(n−1)∗(n−2)∗.....2∗1n!=n∗(n−1)∗(n−2)∗.....2∗1.

For example, 5!=5∗4∗3∗2∗1=1205!=5∗4∗3∗2∗1=120 so we'd return 120.

Assume is nn is a non-negative integer.

'''

def factorial(n):
  fact=1
  while(n!=0):
    fact=fact*n
    n=n-1
  return fact

print(factorial(5))
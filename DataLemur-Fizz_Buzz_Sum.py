'''
Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.

For example, if the target value was 10, the multiples of 3 or 5 below 8 are 3, 5, 6, and 9.

Because 3+5+6+9=233+5+6+9=23, our function would return 23.

'''
#Intialise i and sum 
#Loop till less than target
#if divisible by 3 or 5, add to sum 
#increment i 

def fizz_buzz_sum(target):
  i=2
  sum=0
  while(i<target):
    if((i%3==0) or (i%5==0)):
      sum+=i
    i+=1
  return sum

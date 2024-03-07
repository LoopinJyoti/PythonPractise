'''
Given an input list containing nn distinct numbers in the range 0 to nn, return the only number in the range that is missing from the list.

For example, given input = [0,1,3], return 2. Because the input list has 3 elements in it, we expect to see the numbers 0 to 3 in there, but 2 is missing.

Another example: given input = [4, 3, 2, 1], return 0. We return 0 becuase the input list has 4 elements in it, so we expect to see the numbers 0 to 4 in there, but 0 itself is missing!
'''

def missing_int(input: list[int])-> int:
  
  hashmap = {}
  for ele in input:
    hashmap[ele]= 1
  n = len(input)
  lst = [i for i in range(0, n+1)]
  for k in lst:
    if k not in hashmap:
      return k
  return 

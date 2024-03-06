'''
Write a function to get the intersection of two lists.

For example, if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3].
'''

#Loop through list1
#Loop through list2
#Comparing each element of list1 with each element of list2, if equal add to common list

def intersection(a, b):
  common = []
  for i in a:
    for j in b:
      if(i==j):
        common.append(j)
  return common
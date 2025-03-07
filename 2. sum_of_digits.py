'''
 Write a Python program that takes a list of integers as input and returns a new list where each element
 represents the sum of its digits.
 Sample Input:
 numbers = [2, 25, 756, 24, 111]
 Sample Output:
 [2, 7, 18, 6, 3]
'''

# numbers = [2, 25, 756, 24, 111]
numbers = eval(input('enter the list'))
new_list = []
for i in numbers:
  sum = 0
  for j in str(i):
    sum += int(j)
  new_list.append(sum)

print(new_list)
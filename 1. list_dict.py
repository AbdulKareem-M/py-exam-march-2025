'''
1. Task:
 Create a Python program that takes a list of words and returns a dictionary where keys are words, and values
 are their lengths. Use loops and string methods.
 Sample Input:
 words = ["apple", "banana", "cherry"]
 Sample Output:
 {'apple': 5, 'banana': 6, 'cherry': 6}
 
'''

# words = ["apple", "banana", "cherry"]
words  = eval(input('enter the list of strings:'))

new = {}

for i in words:
  new[i] = len(i)

print(new)


'''
 5. Task:
 Write a Python function that takes a sentence and returns a dictionary where:- Keys are words in the sentence.- Values are dictionaries containing:
  - 'length' -> Length of the word.
  - 'is_palindrome' -> True if the word is a palindrome, otherwise False.
  - 'count' -> Number of occurrences of the word.
 Sample Input:
 sentence = "madam and racecar are level racecar madam"
 Sample Output:
 {
    'madam': {'length': 5, 'is_palindrome': True, 'count': 2},
    'and': {'length': 3, 'is_palindrome': False, 'count': 1},
    'racecar': {'length': 7, 'is_palindrome': True, 'count': 2},
    'are': {'length': 3, 'is_palindrome': False, 'count': 1},
    'level': {'length': 5, 'is_palindrome': True, 'count': 1}
 
'''

sentence = "madam and racecar are level racecar madam"
new_dict = {}
for i in sentence.split():
  new_dict[i] = {'length':len(i),'is_palindrome':True if i==i[::-1] else False, 'count':sentence.count(i)}
print((new_dict))
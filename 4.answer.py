'''
4. Task:
 Write a Python program that takes a paragraph as input and performs the following using loops,
 decision-making, string methods, sets, and dictionaries:- Count the frequency of each word (ignore case).- Find the longest word.- Find unique words and store them in a set.- Find words that appear more than once.
 Sample Input:
 text = "Python is great. Python is easy. Learning Python is fun!"
 Sample Output:
 Word Frequency: {'python': 3, 'is': 3, 'great.': 1, 'easy.': 1, 'learning': 1, 'fun!': 1}
 Longest Word: 'Learning'
 Unique Words: {'great.', 'is', 'learning', 'easy.', 'python', 'fun!'}
 Repeated Words: {'python', 'is'}
'''

text = "Python is great. Python is easy. Learning Python is fun!"
new_text = text.split()
word_frequency = {}
for i in new_text:
    word_frequency[i] = text.count(i)
print(word_frequency)

count = 0
for i in new_text:
  if len(i)>count:
    count = len(i)
    longest_word = i
print(longest_word)

print(set(new_text))

elements = []
for i in new_text:
  if new_text.count(i)>1:
    elements.append(i)
print(set(elements))
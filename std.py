# coding:utf-8
import base64
from collections import namedtuple
from collections import Counter
import heapq
import itertools
import os.path
from os.path import dirname

content = ('Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a '
           'lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of '
           'knowledge, exceeds the short vehemence of any carnal pleasure.')

# base64 encode
# print(base64.encode(content, value=base64.b64encode, sep='\n'))

Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('♠', 'A')
card2 = Card('♥', '2')
print(card2, card1)

words = ['This', 'is', 'a', 'collection', 'of', 'words', '.']

counter = Counter(words)
for elem, count in counter.most_common(1):
    print(elem, count)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
list2 = [{'name': 'Alice', 'age': 30}, {'name': 'Beth', 'age': 25}, {'name': 'Cecil', 'age': 25},
         {'name': 'Diana', 'age': 35}, {'name': 'Eve', 'age': 28}]
print(heapq.nlargest(2, list2, key=lambda x: x['age']))

for value in itertools.permutations('abcd'):
    print(value)

for value in itertools.combinations('abcd', 3):
    print(value)

for value in itertools.product('abcd', '1234', '908'):
    print(value)

print(dirname('tu.py'))

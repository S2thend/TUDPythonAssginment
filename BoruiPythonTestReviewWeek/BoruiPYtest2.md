# Program Structure
```py
# 1.get a list of documents from file
def getDocuments()->list:
# 2.construct the dict from the list of documents
def getDict( documents:list )->dict:
#3.using input words to find sets(doc_numbers..) from the dict and get intersection of sets
def findWordsIntersect( db:dict, words:string )->string:
# 4.Menu 
while True:
```
# Data Structure
1. dict using word as key, and set of document numbers as value
2. list for documents, each document as an element

# Difficulty
1. Use .strip(string.punctuation).lower() to process words before using words as keys.
2. While using new doc.. as deliminator, the first element is empty string and must not be appended.
3. However the last element must be appended manually since no new doc.. following it.
4. While adding dict elements, if no element found, create new set. Two solutions for this: First, use if.. in... Second, use try..catch.., if try .add() error create new set in except block.
5. While intersecting sets, if one is empty set, just return no results, because any sets intersect with empty is empty.
6. To continueously intersect sets with forloop, using a temperary wordset to store the last intersecting result,and intersect with current set, since intersection is independent of sequential orders.
Lab 8 - Lists
Content: Lists, Python functions, if-else statements, loops, strings
 
Questions:

1. Write a Python function to sum all numbers in a list.
Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: 21
```py
print( sum( [1, 2, 3, 4, 5, 6] ) )
```

2. Write a Python function to get the largest number from a list. 
Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: 6
```py
print( max( [1, 2, 3, 4, 5, 6] ) )
```

3. Write a Python function that takes a list of words and counts how many
of them begin with ‘o’.
Sample list: ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
Expected Output: 2
```py
count =0
for el in ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']:
    if el[0] == "o":
        count += 1
print(count)
```


4. (modify Ex3) Write a Python function that takes a list of words and a
character, and counts how many of the words in the list begin with that character.
```py
def findFirstLetter (i):
    count =0
    for el in ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']:
        if el[0] == i:
            count += 1
    print(count)
findFirstLetter("t")
```

5. Write a Python function that takes a list of numbers and returns a
new list containing only the even numbers from the first list.
Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: [2, 4, 6]
```py
Sample = [1, 2, 3, 4, 5, 6]
filtered = filter(lambda elementInSample: (elementInSample+2)%2 == 0, Sample)
print(list(filtered))
```


6. Create a list of 100 integers whose value and index are the same, e.g., L[5]=5.
```py
li = []
for i in range(0,100):
    li.append(i)
print(li)
```

7. Write a Python program to remove duplicates from a list.
Sample list: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]. Expected Output: [1, 2, 3, 4, 5, 6]
```py
sample = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
set = set()
for el in sample:
    set.add(el)
print(list(set))
```

8. Write a Python function that takes two lists and returns True if they have at least one common member.
Sample list: [1, 2, 3, 4, 5, 6] and [10, 9, 8, 7, 6]. Expected Output: True
```py
sample = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
set = set()
for el in sample:
    set.add(el)
print(list(set))
```

9. Write a Python program to get the difference between the two lists.
Sample list: [1, 2, 3, 4, 5, 6] minus [10, 9, 8, 7, 6]
Expected Output: [1, 2, 3, 4, 5]
Sample list: [10, 9, 8, 7, 6] minus [1, 2, 3, 4, 5, 6]
Expected Output: [10, 9, 8, 7]
```py
sample = [1, 2, 3, 4, 5, 6]
sampleMinus = [10, 9, 8, 7, 6]
set = set()
for el in sampleMinus:
    set.add(el)
filtered = filter(lambda elementInSample:not(elementInSample in set) , sample)
print(list(filtered))
```

10. Write a Python program to convert a list of multiple integers into a single integer. 
Sample list: [11, 33, 50]
Expected Output: 113350
```py
print( ("").join( str(x) for x in [11, 33, 50] ) )
```

11. Given a list of integers, write a Python function to create a new list with the same number of elements in the original list such that each integer in the new list is the sum of its neighbours and itself. For example, if  listA = [10,20,30,40,50], new_list =[30,60,90,120,90]
```py
listA = [10,20,30,40,50]
new_list = []
lastValue = 0

for index,value in enumerate(listA):
    if index == 0:
        new_list.append(value+listA[1])
    elif index == len(listA)-1:
        new_list.append(value+listA[-2])
    else:
        new_list.append(value+listA[index-1]+listA[index+1])
print(new_list)
```

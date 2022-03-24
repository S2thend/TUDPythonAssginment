Lab 13 - More on functions
Questions:
 
1. What is the difference between an argument and a parameter?
    ```
    Parameters are a placeholders of actual arguments. 
    Parametera are defined during declaration of functions.
    Arguments are the values passed to functions during function executions.
    ``` 

2. What does the following code print? 

    ```py
    def my_function(b_list):
    b_list[0] = 100
    a_list = [1,2,3]

    a_list = [5,6,7]
    my_function(a_list)
    print(a_list) #Output is [100, 6, 7]
    ```

3. What does the following code print? Explain.
    ```py
    def f(a, b=2):
        pass

    f(a=3, b=4)
    print(a, b)
    # NameError: name 'a' is not defined
    # Because a,b are created in the local scope during function decalartion. 
    ```
4. Consider the following code. The “print(x)” statement generates an error. Provide two different ways to print “x” properly.
    ```py
    def add_one(number):
        x=1
        number = number + x
        print(number)

    add_one(3)
    print(x)

    #S1
    def add_one(number):
        x=1
        number = number + x
        print(number)
        return x

    x = add_one(3)
    print(x)

    #S2
    x = 0
    def add_one(number):
        global x 
        x=1
        number = number + x
        print(number)

    add_one(3)
    print(x)
    ```
5. Give the output indicated for the following program. It will be helpful to draw diagrams to indicate the relationships among arguments, parameters, and their objects. Think about which arguments are mutable and which are immutable.
```py
def func1(list1, list2, str1):
   if len(list1) > 3:
       list1 = list1[:3]
   list2[0] = 'goodbye'
   str1 = ''.join(list2)

arg1_list = ['a', 'b', 'c', 'd']
arg2_list = ['hello', 'mother', 'and', 'father']
arg_str = 'sister'

func1(arg1_list, arg2_list, arg_str)

print(arg1_list)  # Line 1
print(arg2_list)  # Line 2
print(arg_str)  # Line 3
```

(a) What output is produced by Line 1 when the program is executed?         

    ['a', 'b', 'c', 'd']


(b) What output is produced by Line 2 when the program is executed?

    ['goodbye', 'mother', 'and', 'father']

(c) What output is produced by Line 3 when the program is executed?

    sister


6. Remove odds or evens:

(a) Write a function that takes a list of integers as an argument, removes even numbers from the list, and returns the modified list.
```py
from typing import *

def removeNum(nums:List[int])->List[int]:
    for i, v in enumerate(nums):
        if (v+2) % 2 == 0:
            del nums[i]
    return nums

print(removeNum([1,2,3,4,5,6,7,8,9]))
```
(b) Write a function that takes a list of integers as an argument, removes odd numbers from the list, and returns the modified list.
```py
from typing import *

def removeNum(nums:List[int])->List[int]:
    for i, v in enumerate(nums):
        if (v+2) % 2 == 0:
            pass
        else:
            del nums[i]
    return nums

print(removeNum([1,2,3,4,5,6,7,8,9]))
```
(c) Write a function that takes a list of integers and a Boolean as arguments. If the
Boolean is True, the function removes odd numbers from the list; otherwise, evens
are removed. The function returns the modified list.
```py
from typing import *

def removeNum(opt:bool, nums:List[int])->List[int]:
    if opt:
        for i, v in enumerate(nums):
            if (v+2) % 2 == 0:
                del nums[i]
    else:
        for i, v in enumerate(nums):
            if (v+2) % 2 == 0:
                pass
            else:
                del nums[i]
    return nums

print(removeNum([1,2,3,4,5,6,7,8,9]))
```
 
7. A palindrome is a word that is the same backward as forward. The word rotor is an example of a palindrome.
 
(a) Write a function that returns True if two strings are palindromes. (Hints: You can
create a list from a string using the list() function. Lists are handy, because there
is a reverse() method.)
```py
def isPalindrome(a:str, b:str)->bool:
    la = list(a)
    lb = list(b)
    lar = list(a)
    lar.reverse()
    lbr = list(b)
    lbr.reverse()
    print(la)
    print(lar)
    if(lar!=la or lbr!=lb):
        return False
    return True
print(isPalindrome("ababa","qwedewq"))
```
(b) Write a program that uses your function. The program should prompt for the two
strings, call the function, and then print results (something other than True or
False).
```py
input1 = input("Enter a word:")
input2 = input("Enter another word:")

if isPalindrome(input1,input2):
    print("Both words are palindromes.")
else:
    print("Not both words are palindromes.")
```
(c) Some palindrome rules ignore spaces and capitalization, so “Never odd or even” is an acceptable palindrome. Improve your function to ignore spaces and capitalization.
(Hints: Lists have a remove() method, and strings have a lower() method.)
```py
def isPalindrome(a:str, b:str)->bool:
    la = list(a.lower())
    lb = list(b.lower())
    try:
        while True:
            la.remove(' ')
    except ValueError:
        pass
    try:
        while True:
            lb.remove(' ')
    except ValueError:
        pass
    lar = la[::-1]
    lbr = lb[::-1]
    print(la)
    print(lar)
    if(lar!=la or lbr!=lb):
        return False
    return True
print(isPalindrome("aBa   ba","qwedewq"))
```

8. Write a function that takes a list as an argument and veriﬁes whether the list is sorted. Return True if sorted; False if not.
```py
def isSorted(list):
    for i in range(0,len(list)-1):
        if(list[i]>list[i+1]):
            return False
    return True
```
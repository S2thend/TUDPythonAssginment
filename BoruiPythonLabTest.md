Question 1:

Write a program to encrypt a string. The encryption should work as follows: every character in the string gets replaced with the character with ASCII code plus the index value of the index.

Example: “Monty Python” becomes “Mppw}%V|qyy”.
First character M (index 0) adds 0 to its ASCII code, resulting in the same character M 
Second character o (index 1) adds 1 to its ASCII code, resulting in character p
Third character n (index 2) adds 2 to its ASCII code, resulting in character p
.
.
.
Last character n (index 11) addes 11 to its ASCII code, resulting in character y.

Your program should prompt the user for a string, encrypt it, and print the encrypted result.

Hint: Use the functions chr() and ord()


Question 2:

Write a Python function that takes as input a string that stores date and time (24-hour clock) in the following format:“DD/MM/YYYY HR:MIN:SEC” and prints the following:

->  DD/MM/YYYY
->  HR:MIN:SEC
->  MM/YYYY
->  Whether the time is a.m. or p.m.

Validation of the input in the function is necessary. For example, if the user gives an input of “04/122/1990 13:12:12”, the given string is invalid, as there can be only 12 months in a year. In this case prints an error message instead. Think of all possible erroneous inputs and write code to handle them. The function doesn’t return anything. Consider the skeleton code below:

import string

def format_time(date_time):
   # function implementation

format_time("21/02/2020 18:06:00")
print()
format_time("37/05/1950 12:00:00")
print()
format_time("01/01/1900 25:06:00")

The output of this code could be:

-> 21/02/2020
-> 18:06:00
-> 02/2020
-> p.m.

Days are wrong

Hour is wrong


Hints: (1) Use the split() function and its parameter to break down the problem. Use it multiple times if necessary. (2) Once you find an error you can print a message and use the keyword return to leave the function.

Question 3:
In mathematics a positive number is called a Kaprekar number if the representation of the square of the number can be split into two parts (not necessarily of the same length) that add up to the original number (the second part is allowed to start with a leading zero). 
If a number is smaller than 10, it is not a Kaprekar number.
 
For example, 45 is a Kaprekar number as 45*45 = 2025, and 20+25 = 45.
Another Kaprekar number is 55, as 55*55 = 3025, and 30+25 = 55
 
On the other hand 12 is NOT a Kaprekar number, as 12*12 = 144.
We can partition 144 as 1 and 44, or as 14 and 4.
1 + 44 = 45 ≠ 12
14 + 4 = 18 ≠ 12
So there doesn’t exist a partition of 144 where the sum of both parts add up to 12.
 
The Kaprekar numbers from 10 to 1000 are:
10 45 55 99 100 297 703 999
 
(Note: this is an adapted definition of Kaprekars numbers for the purpose of this lab test.)
 
 
YOUR TASK:
 
Write a Python program that will prompt the user for a number, and print all the Kaprekar numbers from 10 up to that number. 
Use functions where appropriate to structure your code. 
 
For example, you may want to implement the following functions:
A function that will take a number and check if it is a Kaprekar number
A function that will take as a parameter a number n and will print all Kaprekar numbers from 10 to n
 
 
Sample output:
 
 


Question 4:

Write a Python function replace_all( ) which replaces all occurrences of a list of words with new words in a string. The function should have three parameters: (1) the string, (2) the list of words to be replaced, and (3) the list of words to be replaced with.

Example 1:   replace_all(‘This is a wonderful morning.’, [‘is’], [‘was’])
should produce the string
‘This was a wonderful morning.’
replacing each instance of ‘is’ with ‘was’.

	
Example 2:
replace_all(‘This is a wonderful morning.’, [‘is’, ‘morning’], [‘was’, ‘evening’]) 

should produce the string

‘This was a wonderful evening.’
replacing each occurrence of ‘is’ (from the first list) with ‘was’ (from the 2nd list), and each occurrence of ‘morning’ with ‘evening’


Note that the lists that are the second and third argument of the function are related – for each of the words to be replaced in the first list there is a corresponding replacement word in the second list. 

Example 3:
replace_all(‘John and Bill went to the shop.’,  [‘John’, ‘Bill’, ‘shop’],   [‘Mary’, ‘Ann’, ‘cinema’]) 

will replace all occurrences of John with Mary, all occurrences of Bill with Ann, and all occurrences of shop with cinema, producing the string

‘Mary and Ann went to the cinema.’





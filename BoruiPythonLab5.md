Lab 5 - Strings
Content: if-elif-else, while, strings and string slicing.
 

1. Write a Python program to print each character of a string on a single line.
```python
input_str = input("pls enter a string:")
for char in input_str:
    print(char)
```

2. Write a Python program that will calculate the length of a string
(We already have a function len that does that, but we want to implement our own)

Solution1:
```python
input_str = input("pls enter a string:")
counter = 0
for char in input_str:
    counter += 1
print(counter)
```

Solution2:
```python
from asyncio.windows_events import NULL

input_str = input("pls enter a string:")
index = 0
try:
    while input_str[index] != NULL:
        index += 1
except BaseException:
    print("length is", end=" ")
finally:
    print(index)
```
3. Given the string "Monty Python":  
(a)Write an expression to print the first character.  
```python
print("Monty Python"[0])
```
(b)Write an expression to print the last character.   
```python
print("Monty Python"[-1])
```
(c) Write an expression including len to print the last character.   
```python
print("Monty Python"[len("Monty Python") - 1])
```
(d) Write an expression that prints "Monty".
```python
print("Monty Python"[:5])
```

3. Write a Python program that reads a string and prints a string that is made up of the first two characters and the last two characters. If the string has a length less than 4 the program prints a message on the screen.
 ```python
input_str = input("pls enter a string:")
if(len(input_str) < 4):
    print("less than 4 characters")
else:
    print(input_str[:2]+input_str[-2:])
```

For example: “hello there” will result in “here”

1. Given a variable S containing a string of odd length:   
(a) Write an expression to print the middle character.   
 ```python
input_str = input("pls enter a string:")
print(input_str[len(input_str)//2])
```
(b) Write an expression to print the string up to but not including the middle character
```python
input_str = input("pls enter a string:")
print(input_str[:len(input_str)//2])
```
(i.e., the first half of the string).   
(c) Write an expression to print the string from the middle character to the end (not
including the middle character).
```python
input_str = input("pls enter a string:")
print(input_str[len(input_str)//2:])
```

5. Five string methods manipulate case: capitalize , title , swapcase , upper ,
and lower . Consider the strings: s1 = "concord" , s2 = "souix city" , s3 =
"HONOLULU" , and s4 = "TopHat".   

Describe what capitalize does.   
Turn fisrt char into upper case, turn the rest into lower.

Describe what swapcase does.  
Turn upper cased char into lower case, turn the lower cased into upper.


Describe what upper does.   
Turn all chars into upper case.

Describe what lower does.      
Turn all chars into upper case.

Describe what title does.       
Turn all first char in every word of a sentence into upper, while rest into lower.

6. Write a Python program that will reverse a string (using a loop, not using slicing)
```python
input_str = input("pls enter a string:")
for index in (range( 1, len( input_str )+1 )):
    print(input_str[-index], end="")
```

7. Write a Python program that will “encrypt” a string. The encryption algorithm we’ll use is add 1 to the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc. The string ‘abc’ becomes ‘bcd’. You’ll need to use the functions ord() and chr() discussed in class

```py
input_str = input("pls enter a string:")
encryt_str = ''
for char in input_str:
    encryt_str += chr( ord(char) + 1 )
print(encryt_str)
```
Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98) and find the
character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’ 

8. We are going to look at some conversions from integer to binary and then from binary back to integer. Prompt the user for an integer, convert the integer to a binary number string (there is no type for actual binary numbers so we just represent it as a string). If you are not familiar with binary numbers have a look on this link https://www.mathsisfun.com/binary-number-system.html


In the second part of the exercise we’ll take the binary string representation and we will convert it back into an integer. 

Part1, Solution1
```py
input_str = input("pls enter a integer:")
input_int = int(input_str)
if input_int == 0:
    print("0")
elif input_int < 0:
    print("negative number")
else:
    binary = ''
    while input_int != 0:
        remainder = str(input_int%2)
        input_int = input_int//2
        binary = remainder + binary
    print(binary)
```
Part1, Solution2:
```py
input_str = input("pls enter a integer:")
binary = bin(int(input_str))
print(binary)
```
Part2, Solution1:
```py
input_str = input("pls enter a string:")
dec = 0
counter = len(input_str) - 1
for char in input_str:
    dec += int(char) * 2 ** counter
    counter -= 1
print(dec)
```
Part2, Solution2:
```py
input_str = input("pls enter a binary:")
print(int(input_str,2), "is the result.")
```

 
Things to remember:
 
If the integer is 0, then we are done since conversion back and forth of 0 is still 0. The program simply prints a note saying it is 0 and quits.
 
If the integer is negative, then we probably don’t know how to do it, so the program prints a message saying it is negative and quits.
 
Otherwise, we do the conversion of the integer to a binary string (a string of 1s and 0s) and then convert that same string back to an integer to make sure we did it right.
 
 
Hints
How do we get a binary string from an integer? 
 
To convert an integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient and the remainder. Continue dividing the quotient by 2 until you get a quotient of zero. Then just write out the remainders in the reverse order.
 
Here is an example of such conversion using the integer 12. 
First, let’s divide the number by two specifying quotient and remainder:
 
12 / 2 = 6, remainder 0
6 / 2 = 3, remainder 0
3 / 2 = 1, remainder 1
1 / 2 = 0, remainder 1
 
Now, we simply need to write out the remainder in the reverse order — ‘1100’. So, 12 in the decimal system is represented as ‘1100’ in binary.
 
How do we get an integer from a binary string? 
 
We know it is a string, so the elements are ‘1’ and ‘0’. Every time we grab a 1 or a 0 (a bit), we are adding a power of two to the overall integer value. Which power of 2? If you grab bits from the right, they are increasing orders of powers of 2. The far right position of the string, or, better said, the last bit in the string (how do you get the last bit??) is 2**0. The next bit 2**1. The next bit 2**2. And so on. If the bit is a ‘1’, then we add that power of 2 to the overall sum; if it is 0 we do nothing.
 

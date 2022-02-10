Lab 6 - More Strings
Content: if-elif-else, while, strings, string slicing, string methods.

1. It is possible to combine string methods in one expression. Given the expression s=
"CAT" , what is s.upper().lower() ?

>Output is cat

2. Using the input command, prompt for input and then convert the input to lowercase.

```py
input_str = input("pls enter a string:")
print(input_str.lower())
```

3. Experiment with the count method. What does it count? For example,

some_string = "Hello world!"
some_string.count("o")

>Output is 2

4. Experiment with the strip method. What does it do? For example,

some_string = "Hi!......"
some_string.strip(".!")

>Output is Hi. It gets rid of every . and !

5.  (a) Suppose you want to print a line full of '#' characters. For simplicity, let’s say that a
line can have only 80 characters. One way is to create a long string to be printed. How
would you do it more elegantly in Python using the plus operation (+) of strings?
```py
str = ""
for i in range(80):
    str = "#" + str
print(str.count("#"))
```

(b) Suppose you want to print a column full of '#' characters. For simplicity, let’s
say that a column could have only 30 characters. Similar to (a), how would you do
it more elegantly in Python using the multiply operation (*) of strings? Hint: Use
the newline character (‘\n’).
```py
print(("#" + "\n") * 30)
```

6. Suppose you have a string ab_string = 'abababababababab' . Write an
expression to remove all the b’s and create a string string = 'aaaaaaaa' .
```py
ab_string = 'abababababababab'
print(''.join(ab_string.split('b')))
```

7. Although Python’s formatted printing can be cumbersome, it can often drastically
improve the readability of output. Try creating a table out of the following values:

Melting and Boiling Points of Alkanes
Name		Melting Point (deg C)		Boiling Point (deg C)
Methane	-162				-183
Ethane		-89				-172
Propane	-42				-188
Butane		-0.5				-135
```py
print("{:10s}{:>22s}{:>22s}".format( "Name","Melting Point (deg C)","Boiling Point (deg C)"))
print("{:10s}{:>22.2f}{:>22.2f}".format("Methane", -162, -183))
print("{:10s}{:>22.2f}{:>22.2f}".format("Ethane", -89, -172))
print("{:10s}{:>22.2f}{:>22.2f}".format("Propane", -42, -188))
print("{:10s}{:>22.2f}{:>22.2f}".format("Butane", -0.5, -135))
```

8. Write a Python program that will swap two random letters in a string.
Hint: Random letters means “letters with random index”
random.randint(x,y) will return a random number in the range from x to y inclusive.
You need to import random at the top of your program. You’ll also need to use slicing
– splitting your string into substrings.
```py
from random import randint

input_str = input("pls enter a string:")
index1 = randint(1, len(input_str))
index2 = randint(1, len(input_str))
if index1 == index2:
    print(input_str)
else:
    if(index1 > index2):
        index1, index2 = index2, index1
    print(index1,index2)
    print(input_str[:(index1-1)]+input_str[index2-1]+input_str[index1:(index2-1)]+input_str[index1-1]+input_str[index2:])
```

9. Pig Latin
Pig Latin is a game of alterations played on words. To make the Pig Latin form of an
English word the initial consonant sound is transposed to the end of the word and an
“ay” is affixed. Specifically there are two rules:
(a) If a word begins with a vowel, append “yay” to the end of the word.
(b) If a word begins with a consonant, remove all the consonants from the beginning
up to the first vowel and append them to the end of the word. Finally, append “ay”
to the end of the word.

```py
input_str = input("pls enter a string:")

if input_str[0] in "aeiou":
    print(input_str+"yay")
else:
    for index in range(1,len(input_str)):
        if input_str[index] in "aeiou":
            print(input_str[index:] + input_str[:index] +'ay')
```

For example:
dog ⇒ ogday
scratch ⇒ atchscray
is ⇒ isyay
apple ⇒ appleyay

Write a program that repeatedly prompts for an English word to translate into Pig
Latin and prints the translated word. If the user enters a period, halt the program.
Hints:
Slicing is your friend: it can pick off the first character for checking, and you can slice
off pieces and concatenate to yield the new word.
Making a string of vowels allows use of the in operator: vowels = ' aeiou' .

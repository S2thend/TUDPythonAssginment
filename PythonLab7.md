Lab 7 - Functions
Content: Python functions, if-else statements, loops, strings
 
Questions:

1. Write a function that takes a number as a parameter and prints the
numbers from 1 to that number on the screen.
```py
def number_count(num):
   for i in range(1,num+1):
       print(i)
number_count(10)
```

2. Write a function that takes a number as a parameter and iterates from 0
to that number. For each iteration, it will check if the current number is even or odd,
and report that to the screen (e.g. “1 is odd”, “2 is even”).
```py
def number_count(num):
   for i in range(0,num+1):
       if (i+2)%2 == 0:
           print(str(i) , 'is even')
       else:
           print(str(i) , 'is odd')
number_count(10)
```

3. Write a function that takes a number as a parameter, iterates from 0 to
that number, and for each iteration of the loop, multiplies the current number by 9
and prints the result (e.g. “2 * 9 = 18”).
```py
def number_count(num):
   for i in range(0,num+1):
       print(str(i), '*', '9', '=', str(i*9))
number_count(10)
```

4. Write a function that asks the user for a number and prints the sum of all
numbers from 1 to the number they enter.
```py
def number_count():
    input_int = int(input('pls enter a inteager:'))
    sum = 0
    for i in range(0,input_int+1):
        sum += i
    print(sum)
number_count()

```

5. Write a function to print a factorial of a number.
```py
def number_factorial():
    input_int = int(input('pls enter a inteager:'))
    f = 1
    for i in range(1,input_int+1):
        f *= i
    print(f)
number_factorial()

```

6. Write a function that takes a string as a parameter and returns a string that is made up of the first two characters and the last two characters. If the string has a length less than 4 the program prints a message on the screen. For example: “hello there” will result in “here”
```py
def word():
    input_str = input('pls enter a word:')
    if len(input_str) >= 4:
        print(input_str[:2]+input_str[-2:])
    else:
        print('less than 4 char')
word()
```

7. Write a Python program to remove the characters which have odd index
values of a given string. The function should return the new string.
```py
def word():
    input_str = input('pls enter a word:')
    output = ''
    for index, value in enumerate(input_str):
        if (index+2)%2 ==0 :
            output += value
    return output
print(word())
```

8. Write a Python function to get the first half of a specified string of even length.
Sample function and result: 

string_first_half(“Python”) 
should return Pyt
```py
def word():
    input_str = input('pls enter a word:')
    print(input_str[:(len(input_str)//2)])
word()
```

9. Write a Python function to insert a string in the middle of a string.
Sample function and result: 

insert_string_middle(“{{}}”,”PHP”)
Should return {{PHP}}

```py
def insert_string_middle(a,b):
    print(a[:(len(a)//2)] + b + a[-(len(a)//2):])
insert_string_middle('{{}}','PHP')
```

10. Write a Python function that takes a string and two indices, and returns
a string with the part between the indices removed.
For example: remove_substring(“Hello there”, 2, 6) should return “Hehere”

```py
def remove_substring(a,b,c):
    result= a[:b] + a[(c+1):]
    return result
print(remove_substring('Hello there', 2, 6))
```

11. Heap of Beans:
We are going to play a game called the heap of beans. You start with a heap of beans (we will start with 16 beans) and two players. Each player can remove 1, 2, or 3 beans from the pile of 16. Each player is required to take some number of beans from the pile during each turn. The players take turns removing beans, and the player who takes the last bean from the pile is the loser. You can try this game with a partner using 16 pieces of paper as beans.
Each player is to be represented by a function, so we will have two functions. Each function takes a single argument, representing the present number of beans, and returns the number of beans remaining after the player function takes its turn. During the operation of the player function, the function reports (prints) how many beans were removed. Note that the function decides how many beans to remove. It takes no input from the user.

You also need a main program. The main program initialises the heap of beans to
16 and then alternately calls the first player function and the second player function
until one of them gets the last bean. The main then reports who the loser is and exits.

(a) Write a simple player function such as one that always takes exactly one bean. It
isn’t very interesting, but it lets you test your program.
(b) Now for the fun part. Write a “smart player” function and test it against other
students’ functions in your class.


```py
def main():
    print('start')
    beans = 16
    while beans != 0:
        beans = player1(beans)
        beans = player2(beans)

def player1(beans):
    beans -= 1
    print(beans)
    if beans == 0:
        print('player1')
    return beans

def player2(beans):
    beans -= 1
    print(beans)
    if beans == 0:
        print('player2')
    return beans

main()
```

```py
def player4(beans):
    if beans <=3:
        beans = 0
    elif 5 < beans <=8:
        if 0<(beans-5)<=3:
            beans = 5
    else:
        beans -=1
    if beans == 0:
        print('player4')
    print(beans)
    return beans
```


Lab 3: If-else, if-elif-else, repetition


Objective:
The objective is to practice the concepts of conditionals and repetitions in Python.

Questions:

1. Prompt the user to enter a mark between 0 and 100 and to print “This is a pass” if the mark is 40 or over, and “This is a fail” if the mark is below 40. Hint: use >=

```python
flag = True
while flag:
    inputValue = input("pls enter your score:")
    try:
        score = float(inputValue)
        if ((score <= 100.0) and (score >=40.0)):
            print("you passed")
        elif ((score >= 0.0) & (score < 40.0)):
            print("you failed")
        else:
            print("you are joking")
    except ValueError as inputValue:
        print("Incorect value for", inputValue)
    except BaseException:
        print("unkown error")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

2. Prompt the user to enter two integer numbers, and output if the first is larger, smaller or equal to the second one. Use if-elif-else
```python
flag = True
while flag:
    v0 = float(input("pls enter first number:"))
    v1 = float(input("pls enter second number:"))
    if v0 > v1:
        print("1st larger")
    elif v0 = v1:
        print("two equals")
    else v0 < v1:
        print("2nd larger")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

3. Write a small calculator simulator – ask the user to enter two numbers and an operation (+, -, *, /), and either add, subtract, multiply or divide the numbers, and print the result.
```python
flag = True
while flag:
    v = input("pls enter two numbers followed by a operator(split by comma e.g 1,2,+):")
    m = v.split(",")
    m[1] = float(m[1])
    m[0] = float(m[0])
    if m[2] == "+":
        print(m[0]+m[1])
    elif m[2] == "-":
        print(m[0]-m[1])
    elif m[2] == "*":
        print(m[0]*m[1])
    elif m[2] == "/":
        print(m[0]/m[1])
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

4. Prompt the user for three numbers and print which is the largest of the three.
```python
flag = True
while flag:
    v = input("pls enter 3 numbers(split by comma e.g 1,2,3):")
    m = v.split(",")
    for el in m:
        float(el) 
    print(max(m))
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

5. What output occurs for the following program on the given input?

user_str = input("Enter a positive integer:") # Line 1
my_int = int(user_str)
count = 0
while my_int > 0:
   if my_int % 2 == 1:
       my_int = my_int//2
   else:
       my_int = my_int - 1
   count += 1 # Line 2
print(count) # Line 3
print(my_int) # Line 4

(a) Given user input of 11, what value is output by # Line 3 of the program?
## Answer is 4
(b) Given user input of 12, what value is output by # Line 4 of the program
## Answer is 0
(c) What type is referenced by (associated with) user val in # Line 1 of the program?
## Answer is String
(d) What is the purpose of the = (equal sign) on #Line 2 of the program?
## Give count a new value
(e) What is the purpose of the : (colon) at the end of the while statement?
## Signing the Begin of the while block

6. How many three-digit numbers are divisible by 17? Write a program to print them.
```python
for num in range(100,999):
    if num % 17 == 0:
        print(str(num))
```
better efficiency:
```python
for num in range(102,999,17):
        print(str(num))
```

7. Sum of consecutive integers
(a) Write a program that prompts for an integer — let’s call it X — and then finds the sum of X consecutive integers starting at 1. That is, if X = 5, you will find the sum of 1 + 2 + 3 + 4 + 5 = 15.
```python
flag = True
while flag:
    v = int(input("pls enter an integer:"))   
    print(sum(range(1,v+1)))
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

(b) Modify your program by enclosing your loop in another loop so that you can find consecutive sums. For example, if 5 is entered, you will find five sums of consecutive numbers:
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
```python
flag = True
while flag:
    v = int(input("pls enter an integer:"))
    for m in range(1,v+1):
        print(sum(range(1,m+1)))
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

(c) Modify your program again to only print sums if the sum is divisible by the number of operands. For example, with the sum 1 + 2 + 3 + 4 + 5 = 15, there are five operands and the sum, 15, is divisible by 5, so that sum will be printed. (Do you notice a pattern?)
```python
flag = True
while flag:
    v = int(input("pls enter an integer:"))
    s = sum(range(1,v+1))
    if s % v == 0:
        print(s)
    else:
        print("Not qualified")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

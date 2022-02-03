Lab 4: More if-else, if-elif-else, and loops
 
Objective:
The objective is to practice the concepts of conditionals and repetitions in Python.


Questions:


1. What output occurs for the following program on the given input?
 
int_str = input("Please give me an integer:")
first_int = int(int_str)
int_str = input("Please give me a second integer:")
second_int = int(int_str)
 
tens_count = 0
loop_count = 0
 
while first_int > 10 and second_int < 20:
   if first_int == 10 or second_int == 10:
       tens_count += 1
   first_int -= 5
   second_int += 5
   loop_count += 1
  
print(tens_count) # Line 1
print(loop_count) # Line 2
print(first_int) # Line 3
print(second_int) # Line 4
 
 
(a) Given user input of 20 followed by an input of 10, what value is output by:
i. Line 1 of the program?

<font size="5" color="red"> 1 Line1 </font>

ii. Line 2 of the program?

<font size="5" color="red"> 2 Line2 </font>  

iii. Line 3 of the program?

<font size="5" color="red"> 10 Line3 </font>  

iv. Line 4 of the program?

<font size="5" color="red"> 20 Line4 </font> 

(b) Given user input of 20 followed by an input of 20, what value is output by:
i. Line 1 of the program?

<font size="5" color="red"> 0 Line1 </font> 

ii. Line 2 of the program?

<font size="5" color="red"> 0 Line2 </font> 

iii. Line 3 of the program?

<font size="5" color="red"> 20 Line3 </font> 

iv. Line 4 of the program?

<font size="5" color="red"> 20 Line4 </font> 

(c) What input will cause both first int and second int to be equal to 10
at the end of the program?

2. Write a FOR loop that will iterate from 0 to 20. For each iteration, it will check if the current number is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").
```python
for num in range(1,21):
    if ( num+1 ) % 2 == 0:
        print('number', num, 'is odd')
    else:
        print ('number', num, 'is even')
```
 
3. (a) Write a FOR loop that will iterate from 0 to 10. For each iteration of the loop, it will multiply the number by 9 and print the result (e.g. "2 * 9 = 18").
```python
for num in range(1,11):
    print( num, '*', 9, '=', num*9)
```
(b) Use a nested loop to show the tables for every multiplier from 1 to 10 (100 results total).
```python
for num_a in range(1,11):
    for num_b in range(1,11):
        print(num_a, '*', num_b, '=', num_a * num_b, end = '   ')
    print('')
```
 
4. Write a program to calculate and print the factorial of a number using a FOR loop. The factorial of a number is the product of all integers up to and including that number, so the factorial of 4 is 4*3*2*1= 24
```python
flag = True
while flag:
    input_str = input("pls enter a number:")
    try:
        input_int = int(input_str)
        last_r = 1
        for num in range(1,input_int+1):
            print(num, '*', last_r, '=', end='')
            last_r = num * last_r
            print(last_r, end = '   ')
    except ValueError as inputValue:
        print("Incorect value for", inputValue, "Inteager's only pls")
    except BaseException:
        print("unkown error")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
```

5. What output occurs for the following program on the given input?
 
number_str = input("Enter an int:")
number = int(number_str)
count = 0
 
while number > 0:
   if number % 2 == 0:
       number = number // 2
   elif number % 3 == 0:
       number = number // 3
   else:  # Line 1
       number = number - 1  # Line 2
   count = count + 1
 
print("Count is: ", count)  # Line 3
print("Number is: ", number)  # Line 4
 
(a) Given user input of 9, what value does Line 3 of the program print?

<font size="5" color="red"> Count is:  3 </font> 

(b) Given user input of 9, what value does Line 4 of the program print?

<font size="5" color="red"> Number is:  0  </font>

(c) Given user input of 7, what value does Line 3 of the program print?

<font size="5" color="red"> Count is:  4  </font>

(d) Given user input of 1, what value does Line 3 of the program print?

<font size="5" color="red"> Count is:  1  </font>

(e) If the else clause on Line 1 and Line 2 were removed, what effect would
that have on the program with the input value 1?
i. No effect; the program would give the same results.
ii. The count would be larger.

<font size="5" color="red"> iii. The count would be smaller. </font> 

iv. The while loop would not end.
v. None of the above.
 
6. Ask the user to enter a number and print it back on the screen. Keep asking for a new number until they enter a negative number.


7. Write a program that uses loops to print the triangle below 
Hint 1: you will need to use nested loops.
Hint 2: on line 1 we print 1 *, on line 2 we print 2 stars… on line x we print x stars…)
*
* *  
* * *  
* * * *  
* * * * *  

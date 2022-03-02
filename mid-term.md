Question 1 (5 marks):
Write a Python function that has one parameter, an integer, and print the sum of all its
divisors. A divisor of an integer number n is a number which divides n without remainder.
If a negative number is passed a message should be printed instead.
Your program should also print the divisors that were added. Consider the blueprint code
below:
# Function implementation
# Main code
sum_divisors(20)
sum_divisors(33)
sum_divisors(42)
sum_divisors(-1)
The output in this case should be:
1 + 2 + 4 + 5 + 10 + 20 = 42
1 + 3 + 11 + 33 = 48
1 + 2 + 3 + 6 + 7 + 14 + 21 + 42 = 96
Negative number. Only positive numbers accepted.
Hint: Find out first the sum of the divisors. After that use a string to store the sequence of
numbers being added that needs to be printed.

Question 2 (5 marks):
Write a Python function that will take a text (sentence) and will reverse every second word.
For example, for the input:
I love you for a lifetime
Not only for a day
I love you for who you are
Not what you do or say
the program should produce:
I evol you rof a emitefil
Not ylno for a day
I evol you rof who uoy are
Not tahw you od or yas
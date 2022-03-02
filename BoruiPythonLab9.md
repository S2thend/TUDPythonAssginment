Lab 9 - Copying, tuples and list comprehension
 
Questions:

1. Show the output for the following program. To make it easier, draw a diagram similar to the ones in lecture 9 pdf. 
    ```
    str_list = ['hi', 'mom', 'dad', ['grandma', 'grandpa']]
    new_list = str_list
    copy_list = str_list[:]

    str_list[0] = 'bye'
    new_list[1] = 'mother'
    copy_list[2] = 'father'
    copy_list[-1][0] = 'nanna'

    print(str_list) # Line 1
    print(new_list) # Line 2
    print(copy_list) # Line 3 
    ```

    (a) What output is produced by Line 1 when the program is executed?                 
    ['bye', 'mother', 'dad', ['nanna', 'grandpa']]  
    (b) What output is produced by Line 2 when the program is executed?     
    ['bye', 'mother', 'dad', ['nanna', 'grandpa']]  
    (c) What output is produced by Line 3 when the program is executed?     
    ['hi', 'mom', 'father', ['nanna', 'grandpa']]

2. Consider: 
    ```
    ListA = [1,2,3,4,5]
    ListB = ListA
    ListA[2] = 10
    ```
    What is the value of ListB[2]?  
    [1, 2, 10, 4, 5]


3. Consider the following code: 
    ```
    list1 = [1,2,99]
    list2 = list1
    list3 = list2
    list1 = list1.remove(1)

    print(list3)
    ```

    (a) What is printed?    
    [2, 99]     
    (b) How can you change the code so list3 is unchanged?      
    list3 = list2[:]

4. Given a list L = [1,2,3,4], we want to convert the list to the string '1234'. We tried ''.join([i for i in L]), but it didn't work. Fix it.  
    ('').join([str(i) for i in L])

5. Fractions: You can express a fraction as a tuple: (numerator, denominator).  
    (a) Write a function that adds two fractions that are passed as tuples.   
    ```py
    # tuple(numerator, denominator)
    def addFraction(f1,f2):
        if f1[1] == f2[1]:
            f3 = (f1[0]+f2[0]), f1[1]
        else:
            f3 = (f1[0]*f2[1]+f2[0]*f1[1]), f1[1]*f2[1]
        return f3
    ```  
    (b) Write a function that multiplies two fractions that are passed as tuples    
    ```py
    def mulFraction(f1,f2):
    f3 = f1[0]*f2[0], f1[1]*f2[1]
    return f3
    ```

6. Write a Python program to sort a tuple by its float element.     
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]        
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]        
    ```py
    def sortTuple(t):
        result = sorted(t, key=lambda el:el[1], reverse=True)
        print(result)

    sortTuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])
    ```



7. Using list comprehension     
    (a) Generate a list of square numbers       
    ```py
    list = []
    for num in range(1,10):
        list.append(num**2)
        print(list)
    ```
    (b) Convert a list of colors = ['Red', 'Blue', 'Green', 'Black', 'White'] to upper case     
    ```py
    colors = ['Red', 'Blue', 'Green', 'Black', 'White']
    for i,v in enumerate(colors):
        colors[i] = v.lower()
    print(colors)
    ```
    (c) Find all of the numbers from 1-1000 that are divisible by 7 
    ```py
    list = []
    for num in range(1,1000):
        if num % 7 ==0:
            list.append(num)
    print(list)
    ```
    (d) Find all of the numbers from 1-1000 that have a 3 in them   
    ```py
    list = []
    for num in range(1,1000):
        if str(num).find("3") != -1:
            list.append(num)
    print(list)
    ```
    (d) Count the number of spaces in a string      
    ```py
    str = '  sda  ' 
    count = 0
    for chr in str:
        if chr == ' ':
            count += 1
    print(count)
    ```
    (e) Remove all of the vowels in a string
    ```py
    str = 'abcdefghijklmnopq' 
    list = []
    for chr in str:
        if "aeiou".find(chr) == -1:
            list.append(chr)
    print(('').join(list))
    ```

    (f) Find all of the words in a string that are less than 4 letters
    ```py
    str = 'have a splendid day' 
    list= []
    for el in str.split():
        if len(el) < 4:
            list.append(el)
    print(list)
    ```


    (g) Challenge! Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). The first part is given below. You need to find out the second list comprehension

    [number for number in range(1, 1001) if True in [second list comprehension]]
    ```py
    list = [number for number in range(1, 1001) if [number%div for div in range(2, 10)].count(0) > 1 ]
    print(list)
    ```



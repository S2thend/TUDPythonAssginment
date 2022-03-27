Lab 14 - Classes

Questions:
 
1. Try to answer this question before running the code. You might run it to check your answer. 
```py
class MyClass (object):
   def method1(self, param_list):
       self.local_list = []
       for element in param_list:
           if element > 10:
               self.local_list.append(element)
 
   def method2(self):
       self.sum_int = 0
       for element in self.local_list:
           self.sum_int += element
       return self.sum_int
 

inst1 = MyClass()
inst2 = MyClass()
inst1.method1([1,2,3])
print(inst1.local_list) # Line 1 Output []
inst1.method1([10,11,12])
print(inst1.local_list) # Line 2 Output [11,12]
print(inst1.method2()) # Line 3 Output 23
#inst2.method2() # Line 4 Error local_list doesn't exist
```
(a) What output is produced by # Line 1 of the above program?       
(b) What output is produced by # Line 2 of the above program?           
(c) What output is produced by # Line 3 of the above program?           
(d) # Line 4 is commented out. What result would occur if Line 4 were executed by the program. Why?         
 
 
2. Try to answer this question before running the code. You might run it to check your answer.
```py
class NewClass(object):
   def __init__(self, param_int=1):
       self.the_int = param_int
       if param_int % 2 == 0:
           self.parity = 'even'
       else:
           self.parity = 'odd'
 
   def process(self, instance):
       sum_int = self.the_int + instance.the_int
       if sum_int < 0:
           return 'negative'
       elif sum_int % 2 == 0:
           return 'even'
       else:
           return 'odd'
 
   def __str__(self):
       return 'Value {} is {}'.format(self.the_int, self.parity)
 
 
inst1 = NewClass(4)
inst2 = NewClass(-5)
inst3 = NewClass()
print(inst1)  # Line 1 Output: Value 4 is even
print(inst1.parity)  # Line 2 Output: even
print(inst1.process(inst2))  # Line 3 Output: negative
print(inst3.process(inst1))  # Line 4 Output: odd
```
 
(a) What output is produced by Line 1 of the example program?           
(b) What output is produced by Line 2 of the example program?       
(c) What output is produced by Line 3 of the example program?       
(d) What output is produced by Line 4 of the example program?           
 
 
3. Sample class describing a Person
```py
class Person():
   def __init__(self, fname, sname, address):
       self.f_name = fname
       self.s_name = sname
       self.address = address


   def change_address(self, new_address):
       self.address = new_address

   def __str__(self):
       return self.f_name + " "+ self.s_name + " lives at " + self.address


# main
p1 = Person("John", "Smith", "1 Pinebrook street")
print(p1.f_name)
print(p1.s_name)
print(p1.address)

p1.change_address("5 Cottage Avenue")
print(p1)
```

(a): Design a class to represent a rectangle. Some methods examples can be the rectangle area and rectangle perimeter.

```py
class Rectangle():
   def __init__(self, length1:int, length2:int = None):
        if(length2 == None):
           self.height = length1
           self.width = length1
        else:
            self.width = length1 if length1 > length2 else length2
            self.height = length2 if length1 > length2 else length1


   def get_perimeter(self):
       return (self.height + self.width) *2

   def get_area(self):
       return self.height * self.width

   def __str__(self):
       return "width is " + str(self.width) + ", " + "height is " + str(self.height)

print(Rectangle(6,5))
```

(b): Design a class to represent a bank account. Some information you might want in a bank account are the IBAN, account number, available funds, a list with the last 5 transactions. You might also add methods to withdraw and deposit money.  
```py
class BankAccount():
   def __init__(self, IBAN, account_number, available_funds):
        self.IBAN = IBAN
        self.account_number = account_number
        self.available_funds = available_funds
        self.transactions = []


   def deposit(self, amount):
       self.available_funds += amount
       self.transactions.append(amount)
       if(self.transactions>5):
           del self.transactions[0]
       return self.available_funds

   def withdraw(self, amount):
       self.available_funds -= amount
       self.transactions.append(amount)
       if(self.transactions>5):
           del self.transactions[0]
       return self.available_funds

   def __str__(self):
       return "IBAN: " + str(self.IBAN) + ", " + "ACCN: " + str(self.account_number) + ", " + "Avail:" + str(self.available_funds)
```

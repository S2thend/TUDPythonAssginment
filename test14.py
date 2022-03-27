
# class NewClass(object):
#    def __init__(self, param_int=1):
#        self.the_int = param_int
#        if param_int % 2 == 0:
#            self.parity = 'even'
#        else:
#            self.parity = 'odd'
 
#    def process(self, instance):
#        sum_int = self.the_int + instance.the_int
#        if sum_int < 0:
#            return 'negative'
#        elif sum_int % 2 == 0:
#            return 'even'
#        else:
#            return 'odd'
 
#    def __str__(self):
#        return 'Value {} is {}'.format(self.the_int, self.parity)
 
 
# inst1 = NewClass(4)
# inst2 = NewClass(-5)
# inst3 = NewClass()
# print(inst1)  # Line 1 
# print(inst1.parity)  # Line 2
# print(inst1.process(inst2))  # Line 3
# print(inst3.process(inst1))  # Line 4


import py_compile


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
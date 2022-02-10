# input_str = input("pls enter a integer:")
# input_int = bin(int(input_str))
# binary = ''
# while input_int != 0:
#     remainder = str(input_int%2)
#     input_int = input_int//2
#     binary = remainder + binary
# print(binary)

# input_str = input("pls enter a string:")
# dec = 0
# counter = len(input_str) - 1
# for char in input_str:
#     dec += int(char) * 2 ** counter
#     counter -= 1
# print(dec)

# input_str = input("pls enter a binary:")
# print(int(input_str,2), "is the result.")

# input_str = input("pls enter a string:")
# print(input_str.lower())

# some_string = "Hello world!"
# print(some_string.count("o"))

# some_string = "Hi!......"
# print(some_string.strip(".!"))

# str = ""
# for i in range(80):
#     str = "#" + str
# print(str.count("#"))


# print(("#" + "\n") * 30)

# ab_string = 'abababababababab'
# print(''.join(ab_string.split('b')))

# print("{:10s}{:>22s}{:>22s}".format( "Name","Melting Point (deg C)","Boiling Point (deg C)"))
# print("{:10s}{:>22.2f}{:>22.2f}".format("Methane", -162, -183))
# print("{:10s}{:>22.2f}{:>22.2f}".format("Ethane", -89, -172))
# print("{:10s}{:>22.2f}{:>22.2f}".format("Propane", -42, -188))
# print("{:10s}{:>22.2f}{:>22.2f}".format("Butane", -0.5, -135))

# from random import randint

# input_str = input("pls enter a string:")
# index1 = randint(1, len(input_str))
# index2 = randint(1, len(input_str))
# if index1 == index2:
#     print(input_str)
# else:
#     if(index1 > index2):
#         index1, index2 = index2, index1
#     print(index1,index2)
#     print(input_str[:(index1-1)]+input_str[index2-1]+input_str[index1:(index2-1)]+input_str[index1-1]+input_str[index2:])

input_str = input("pls enter a string:")

if input_str[0] in "aeiou":
    print(input_str+"yay")
else:
    for index in range(1,len(input_str)):
        if input_str[index] in "aeiou":
            print(input_str[index:] + input_str[:index] +'ay')



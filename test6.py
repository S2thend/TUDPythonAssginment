# input_str = input("pls enter a integer:")
# input_int = bin(int(input_str))
# binary = ''
# while input_int != 0:
#     remainder = str(input_int%2)
#     input_int = input_int//2
#     binary = remainder + binary
# print(binary)

input_str = input("pls enter a string:")
dec = 0
counter = len(input_str) - 1
for char in input_str:
    dec += int(char) * 2 ** counter
    counter -= 1
print(dec)

input_str = input("pls enter a binary:")
print(int(input_str,2), "is the result.")
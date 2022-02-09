input_str = input("pls enter a integer:")
input_int = int(input_str)
binary = ''
while input_int != 0:
    remainder = str(input_int%2)
    input_int = input_int//2
    binary = remainder + binary
print(binary)

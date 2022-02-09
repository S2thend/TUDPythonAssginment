from asyncio.windows_events import NULL

input_str = input("pls enter a string:")
index = 0
try:
    while input_str[index] != NULL:
        index += 1
except BaseException:
    print("length is", end=" ")
finally:
    print(index)
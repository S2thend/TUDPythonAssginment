# raw_string = 'Monty Python'
# enc_string = ''
# for i, v in enumerate(raw_string):
#     enc_string += chr(ord(v) + i)
# print(enc_string)

# def format_time(date_time):
#     timeList = date_time.split()
#     if( int(timeList[0][:2])>30 or int(timeList[0][:2])<0 ):
#         print("Days are wrong")
#     elif( int(timeList[0][3:5])>12 or int(timeList[0][3:5])<0 ):
#         print("Weeks are wrong")
#     elif( int(timeList[1][:2])>24 or int(timeList[1][:2])<0 ):
#         print("Hours are wrong")
#     else:
#         print(timeList[0])
#         print(timeList[1])
#         print(timeList[0][3:])
#         print("AM" if int(timeList[1][:2])<12 else "PM")

# format_time("21/02/2020 18:06:00")

# format_time("37/05/1950 12:00:00")

# format_time("01/01/1900 25:06:00")



# def k_check(number_int):
#     number_str = str(number_int**2)
#     if( len(number_str)/2 > len(str(number_int)) ):
#         return
#     else:
#         for i in range( len(str(number_int)) if len(str(number_int)) < len(number_str)-len(str(number_int)) else len(number_str)-len(str(number_int)),len(number_str) ):
#             if( int( number_str[:i] ) + int( number_str[i:]) == number_int ):
#                 print(number_int, "is k number")
#                 break

# input_int = int(input('pls enter a number: '))

# for el in range(10,input_int):
#     k_check(el)

dict = {}
def replace_all(sentence, old, new):
    wordList = sentence.split(".")[0].split()
    for i,v in enumerate(wordList):
        dict.update({v:i})
    print(dict)
    for i,v in enumerate(old):
        wordList[dict[v]] = new[i]
    print((' ').join(wordList) + '.')

replace_all('John and Bill went to the shop.',  ['John', 'Bill', 'shop'],   ['Mary', 'Ann', 'cinema']) 

def k_check(number_int):
    number_str = str(number_int**2)
    for i in range( len(str(number_int)) if len(str(number_int)) < len(number_str)-len(str(number_int)) else len(number_str)-len(str(number_int)),len(number_str) ):
        if( int( number_str[:i] ) + int( number_str[i:]) == number_int ):
            print(number_int, "is k number")
            break

input_int = int(input('pls enter a number: '))

for el in range(10,input_int):
    k_check(el)
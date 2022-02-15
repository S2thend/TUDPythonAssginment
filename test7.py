# def number_count(num):
#    for i in range(1,num+1):
#        print(i)
# number_count(10)


# def number_count(num):
#    for i in range(0,num+1):
#        if (i+2)%2 == 0:
#            print(str(i) , 'is even')
#        else:
#            print(str(i) , 'is odd')
# number_count(10)


# def number_count(num):
#    for i in range(0,num+1):
#        print(str(i), '*', '9', '=', str(i*9))
# number_count(10)


# def number_count():
#     input_int = int(input('pls enter a inteager:'))
#     sum = 0
#     for i in range(0,input_int+1):
#         sum += i
#     print(sum)
# number_count()


# def number_factorial():
#     input_int = int(input('pls enter a inteager:'))
#     f = 1
#     for i in range(1,input_int+1):
#         f *= i
#     print(f)
# number_factorial()


# def word():
#     input_str = input('pls enter a word:')
#     if len(input_str) >= 4:
#         print(input_str[:2]+input_str[-2:])
#     else:
#         print('less than 4 char')
# word()

# def word():
#     input_str = input('pls enter a word:')
#     output = ''
#     for index, value in enumerate(input_str):
#         if (index+2)%2 ==0 :
#             output += value
#     return output
# print(word())


# def insert_string_middle(a,b):
#     print(a[:(len(a)//2)] + b + a[-(len(a)//2):])
# insert_string_middle('{{}}','PHP')


# def remove_substring(a,b,c):
#     result= a[:b] + a[(c+1):]
#     return result
# print(remove_substring('Hello there', 2, 6))



def main():
    print('start')
    beans = 16
    while not(beans <= 0):
        beans = player3(beans)
        beans = player1(beans)

def player1(beans):
    beans -= 1
    print(beans)
    if beans == 0:
        print('player1')
    return beans

def player2(beans):
    beans -= 1
    print(beans)
    if beans == 0:
        print('player2')
    return beans



def player3(beans):

    if beans <=3:
        beans = 0
    elif beans%3 == 0:
        if (beans/3)%2 == 0 :
            beans -= 2
        else:
            beans -=3
    else:
        if (beans//3+1)%2 == 0:
            beans -= 2
        else:
            beans -= 3
    print(beans)
    if beans == 0:
        print('player3')
    return beans

main()






# def my_function(b_list):
#    b_list[0] = 100
#    a_list = [1,2,3]

# a_list = [5,6,7]
# my_function(a_list)
# print(a_list)

# def f(a, b=2):
#     pass

# f(a=3, b=4)
# print(a, b)

# def add_one(number):
#    x=1
#    number = number + x
#    print(number)
#    return number

# x = add_one(3)
# print(x)

# x = 0
# def add_one(number):
#    global x 
#    x=1
#    number = number + x
#    print(number)

# add_one(3)
# print(x)


# x = 0
# def add_one(x, number):
#    x=x
#    x=1
#    number = number + x
#    print(number)

# add_one(x, 3)
# print(x)


# def func1(list1, list2, str1):
#    if len(list1) > 3:
#        list1 = list1[:3]
#    list2[0] = 'goodbye'
#    str1 = ''.join(list2)

# arg1_list = ['a', 'b', 'c', 'd']
# arg2_list = ['hello', 'mother', 'and', 'father']
# arg_str = 'sister'

# func1(arg1_list, arg2_list, arg_str)

# print(arg1_list)  # Line 1
# print(arg2_list)  # Line 2
# print(arg_str)  # Line 3

# from typing import *

# def removeNum(nums:List[int])->List[int]:
#     for i, v in enumerate(nums):
#         if (v+2) % 2 == 0:
#             del nums[i]
#     return nums

# print(removeNum([1,2,3,4,5,6,7,8,9]))



# from typing import *

# def removeNum(nums:List[int])->List[int]:
#     for i, v in enumerate(nums):
#         if (v+2) % 2 == 0:
#             pass
#         else:
#             del nums[i]
#     return nums

# print(removeNum([1,2,3,4,5,6,7,8,9]))


from audioop import reverse
from typing import *

# def removeNum(opt:bool, nums:List[int])->List[int]:
#     if opt:
#         for i, v in enumerate(nums):
#             if (v+2) % 2 == 0:
#                 del nums[i]
#     else:
#         for i, v in enumerate(nums):
#             if (v+2) % 2 == 0:
#                 pass
#             else:
#                 del nums[i]
#     return nums

# print(removeNum([1,2,3,4,5,6,7,8,9]))




# def isPalindrome(a:str, b:str)->bool:
#     la = list(a.lower())
#     lb = list(b.lower())
#     try:
#         while True:
#             la.remove(' ')
#     except ValueError:
#         pass
#     try:
#         while True:
#             lb.remove(' ')
#     except ValueError:
#         pass
#     lar = la[::-1]
#     lbr = lb[::-1]
#     print(la)
#     print(lar)
#     if(lar!=la or lbr!=lb):
#         return False
#     return True
# print(isPalindrome("aBa   ba","qwedewq"))


# input1 = input("Enter a word:")
# input2 = input("Enter another word:")

# if isPalindrome(input1,input2):
#     print("Both words are palindromes.")
# else:
#     print("Not both words are palindromes.")


def isSorted(list):
    for i in range(0,len(list)-1):
        if(list[i]>list[i+1]):
            return False
    return True

print(isSorted([1,3,9,5,7]))
print(isSorted([1,3,5,7]))

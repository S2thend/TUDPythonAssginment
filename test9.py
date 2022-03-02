
# str_list = ['hi', 'mom', 'dad', ['grandma', 'grandpa']]
# new_list = str_list
# copy_list = str_list[:]

# str_list[0] = 'bye'
# new_list[1] = 'mother'
# copy_list[2] = 'father'
# copy_list[-1][0] = 'nanna'

# print(str_list) # Line 1
# print(new_list) # Line 2
# print(copy_list) # Line 3 


# ListA = [1,2,3,4,5]
# ListB = ListA
# ListA[2] = 10
# print(ListB)

# list1 = [1,2,99]
# list2 = list1
# list3 = list2[:]
# list1 = list1.remove(1)

# print(list3)

# L = [1,2,3,4]
# print( ('').join([str(i) for i in L]) )


# tuple(numerator, denominator)
# def addFraction(f1,f2):
#     if f1[1] == f2[1]:
#         f3 = (f1[0]+f2[0]), f1[1]
#     else:
#         f3 = (f1[0]*f2[1]+f2[0]*f1[1]), f1[1]*f2[1]
#     return f3
# print(addFraction((1,2),(1,3)))


# def mulFraction(f1,f2):
#     f3 = f1[0]*f2[0], f1[1]*f2[1]
#     return f3
# print(mulFraction((1,2),(5,6)))


# def sortTuple(t):
#     result = sorted(t, key=lambda el:el[1], reverse=True)
#     print(result)

# sortTuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])


# list = []
# for num in range(1,10):
#     list.append(num**2)
#     print(list)

# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# for i,v in enumerate(colors):
#     colors[i] = v.lower()
# print(colors)

# list = []
# for num in range(1,1000):
#     if str(num).find("3") != -1:
#         list.append(num)
# print(list)

# str = '  sda  ' 
# count = 0
# for chr in str:
#     if chr == ' ':
#         count += 1
# print(count)


# str = 'abcdefghijklmnopq' 
# list = []
# for chr in str:
#     if "aeiou".find(chr) == -1:
#         list.append(chr)
# print(('').join(list))



# str = 'have a splendid day' 
# list= []
# for el in str.split():
#     if len(el) < 4:
#         list.append(el)
# print(list)


list = [number for number in range(1, 1001) if [number%div for div in range(2, 10)].count(0) > 1 ]
print(list)

    
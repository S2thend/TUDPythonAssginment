# my_set = set('bcd')
# your_set = set('abcde')

# print(my_set.issubset(your_set))
# print(your_set.issubset(my_set))


# string2 =  'the big dwarf only jumps'
# string1 =  'given string is Heterogram'
# string1_c = string1.replace(" ", "")
# tmp = set()
# isHetero = True
# for char in string1_c:
#     if char in tmp:
#         isHetero = False
#         break
#     else:
#         tmp.add(char)
# print(isHetero)


# string = 'The quick brown fox jumps over the lazy dog'
# string_c = string.replace(" ", "").lower()
# set1 = set()
# set2 = set()
# for char in string_c:
#     if char in set1:
#         set2.add(char)
#     else:
#         set1.add(char)
# print(set1)
# print(set2)
# print(set1 == set2)

# firstName = 'Sherlock'
# lastName = 'Holmes'
# def common(first, last):
#     set1 = set(first.lower())
#     set2 = set(last.lower())
#     res = list(set1 & set2)
#     return res
# print(common(firstName, lastName))

firstName = 'Sherlock'
lastName = 'Holmes'
def common(first, last):
    set1 = set(first.lower())
    set2 = set(last.lower())
    res = set1 ^ set2
    return res
print(common(firstName, lastName))
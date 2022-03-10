# my_set = set('bcd')
# your_set = set('abcde')

# print(my_set.issubset(your_set))
# print(your_set.issubset(my_set))


string2 =  'the big dwarf only jumps'
string1 =  'given string is Heterogram'

string1_c = string1.replace(" ", "")
tmp = set()
isHetero = True
for char in string1_c:
    if char in tmp:
        isHetero = False
        break
    else:
        tmp.add(char)
print(isHetero)
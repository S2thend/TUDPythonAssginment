# D = {'a':3, 'x':7, 'r':5}
# print(D['x'])
# for key in D.keys():
#     if D[key] == 7:
#         print(key)

# print (D.keys())

# print(D.items())

# list1 = [(k, v) for k, v in D.items()] 

# list2 = [(v, k) for k, v in D.items()] 

# list2.sort()
# print(list2)

# num_dict = {}
# for num in range(1,10):
#     num_dict[num] = num**2
# print(num_dict)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for key in d1.keys():
    if key in d2:
        d3[key] = d1[key] + d2[key]
    else:
        d3[key] = d1[key]
for key in d2.keys():
    if not(key in d3):
        d3[key] = d2[key]
print(d3)


d_num = {'1': 'one', '2': 'two', '3': 'three','4': 'four', '5': 'five', '6': 'six','7': 'seven', '8': 'eight', '9': 'nine','0': 'zero'}
input_str = str(input('enter a integer:'))
out = ''
for i,char in enumerate(input_str):
    out = out + ' ' + d_num[char]

print(out)


capitals = {'Argentina':'Buenos Aires','France':'Paris', 'US': 'Washington D.C.'} 
while(True):
    input_city = input('enter city:')
    input_country = input('enter country:')
    capitals[input_country] = input_city
    input_exit = input('exit?y/n, n to continue')
    if input_exit == 'y':
        break
list_c = [(v, k) for k, v in capitals.items()]
list_c.sort() 
print(list_c)
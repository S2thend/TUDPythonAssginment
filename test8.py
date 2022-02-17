print( sum( [1, 2, 3, 4, 5, 6] ) )


print( max( [1, 2, 3, 4, 5, 6] ) )

count =0
for el in ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']:
    if el[0] == "o":
        count += 1
print(count)

def findFirstLetter (i):
    count =0
    for el in ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']:
        if el[0] == i:
            count += 1
    print(count)
findFirstLetter("t")


sample = [1, 2, 3, 4, 5, 6]
filtered = filter(lambda elementInSample: (elementInSample+2)%2 == 0, sample)
print(list(filtered))

li = []
for i in range(0,100):
    li.append(i)
print(li)

sample = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
set = set()
for el in sample:
    set.add(el)
print(list(set))


from multiprocessing.sharedctypes import Value


sample = [1, 2, 3, 4, 5, 6]
sampleMinus = [10, 9, 8, 7, 6]
set = set()
for el in sampleMinus:
    set.add(el)
filtered = filter(lambda elementInSample:not(elementInSample in set) , sample)
print(list(filtered))


print( ("").join( str(x) for x in [11, 33, 50] ) )

# listA = [10,20,30,40,50], new_list =[30,60,90,120,90]

listA = [10,20,30,40,50]
new_list = []
lastValue = 0

for index,value in enumerate(listA):
    if index == 0:
        new_list.append(value+listA[1])
    elif index == len(listA)-1:
        new_list.append(value+listA[-2])
    else:
        new_list.append(value+listA[index-1]+listA[index+1])
print(new_list)
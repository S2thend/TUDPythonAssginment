count = 1
while True:
    if count == 6:
        break
    count += 1
    for num in range(1,count):
        print('*', end=' ')
    print('')

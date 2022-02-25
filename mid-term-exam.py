def sum_divisors(input):
    if input < 0:
        print('Negative number. Only positive numbers accepted.')
    elif input == 0:
        print('Zero. Only positive numbers accepted.')
    elif input == 1:
        print('1 + 1 = 2')
    else:
        last = input
        i = 1
        sum = 0
        eq_list_small = []
        eq_list_big = []
        while i < last:
            if input % i == 0:
                sum += input/i + i
                last = input/i
                eq_list_small.append(str(i))
                eq_list_big.insert(0,str(int(input/i)))
            i += 1
        print((' + ').join(eq_list_small) + ' + ' + (' + ').join(eq_list_big), '=', int(sum))

print('Answer for Q1:')
sum_divisors(20)
sum_divisors(33)
sum_divisors(42)
sum_divisors(-1)
print('')


def jumbo_sentece(input):
    wordList = input.split()
    for i in range(1,len(wordList),2):
        temp = ''
        for chr in wordList[i]:
            temp = chr + temp
        wordList[i] = temp
    print((' ').join(wordList))

print('Answer for Q2:')
jumbo_sentece('I love you for a lifetime')
jumbo_sentece('Not only for a day')
jumbo_sentece('I love you for who you are')
jumbo_sentece('Not what you do or say')

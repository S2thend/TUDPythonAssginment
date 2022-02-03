flag = True
while flag:
    input_str = input("pls enter a number:")
    try:
        input_int = int(input_str)
        last_r = 1
        for num in range(1,input_int+1):
            print(num, '*', last_r, '=', end='')
            last_r = num * last_r
            print(last_r, end = '   ')
    except ValueError as inputValue:
        print("Incorect value for", inputValue, "Inteager's only pls")
    except BaseException:
        print("unkown error")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False

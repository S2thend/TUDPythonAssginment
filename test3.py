while True:
    input_str = input("pls enter a number:")
    try:
        input_int = int(input_str)
        if input_int < 0:
            break
    except ValueError as inputValue:
        print("Incorect value for", inputValue, "Inteager's only pls")
    except BaseException:
        print("unkown error")

flag = True
while flag:
    inputValue = input("pls enter your score:")
    try:
        score = float(inputValue)
        if ((score <= 100.0) and (score >=40.0)):
            print("you passed")
        elif ((score >= 0.0) & (score < 40.0)):
            print("you failed")
        else:
            print("you are joking")
    except ValueError as inputValue:
        print("Incorect value for", inputValue)
    except BaseException:
        print("unkown error")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False




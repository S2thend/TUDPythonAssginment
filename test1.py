flag = True
while flag:
    v = int(input("pls enter an integer:"))
    s = sum(range(1,v+1))
    if s % v == 0:
        print(s)
    else:
        print("Not qualified")
    exit = input("leave?(y/n)")
    if exit == "y":
        flag = False
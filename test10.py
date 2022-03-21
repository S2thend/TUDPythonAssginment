# while True:
#     # Line 1
#     number_str = input("Input a floating-point number: ")
#     try:
#         if number_str.find(".") != -1:
#             number_float = float(number_str)
#             print("Number is",number_float)
#             break
#         else :
#             raise Exception("Wrong Type")
#     except BaseException:
#         print("wrong type")

# def safe_input(prompt,type):
#     while True:
#         # Line 1
#         input_str = input(prompt)
#         if(type == "int"):
#             try:
#                 return int(input_str)
#             except BaseException:
#                 print("wrong type")
#         elif(type=="float"):
#             try:
#                 return float(input_str)
#             except BaseException:
#                 print("wrong type")
#         else:
#             return input_str

# safe_input("enter:","int")



# def prompt_open(mode):
#     while True:
#         f_name = input("enter filename:")
#         try:
#             f = open(f_name, mode)
#             return f 
#         except IOError:
#             print("file not exist")

# f = prompt_open("r")
# f.close()


    


# number_1 = input("Input 1st number: ")
# number_2 = input("Input 2nd number: ")
# number_3 = input("Input 3rd number: ")
# try:
#     float(number_1)
#     float(number_2)
#     float(number_3)
#     res = number_1/number_2 + number_3
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division")

# reverse each line of the input file in the output file
while True:
    file_str = input("Open what file:")
    try:
        input_file = open(file_str)  # potential user error
        while True:
            try:
                find_line_str = input("Which line (integer):")
                find_line_int = int(find_line_str)  # potential user error
                line_count_int = 1
                for line_str in input_file:
                    if line_count_int == find_line_int:
                        print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
                        break
                    line_count_int += 1
                else:
                    # get here if line sought doesn't exist
                    print("Line {} of file {} not found".format(find_line_int, file_str))
                    input_file.close()
                break
            except ValueError:
                print("Line", find_line_str, "isn't a legal line number.")
        break
    except IOError:
        print("The file", file_str, "doesn't exist.")
print("End of the program")
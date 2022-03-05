Lab 10 - Files and exceptions
 
Questions:
 
1. Given: 
    ```
    number_str = input("Input a floating-point number: ")
    while True:
    # Line 1
    print("Number is",number_float)
    ```
    Write a try/except block in # Line 1 that will keep prompting until a correctly formatted floating-point is entered
    ```py
    while True:
    # Line 1
    number_str = input("Input a floating-point number: ")
    try:
        if number_str.find(".") != -1:
            number_float = float(number_str)
            print("Number is",number_float)
            break
        else :
            raise Exception("Wrong Type")
    except BaseException:
        print("wrong type")
    ```

2. Write a function named safe_input(prompt,type) that works like the Python input function, except that it only accepts the specified type of input. The function takes two arguments:
prompt: str  
type: int, float, str
The function will keep prompting for input until the correct input of the specified type is entered. The function returns the input. If the input was specified to be a number (float or int), the value returned will be of the correct type; that is, the function will perform the conversion. The default for a prompt is the empty string. The default for the type is string.
    ```py
    def safe_input(prompt,type):
        while True:
            # Line 1
            input_str = input(prompt)
            if(type == "int"):
                try:
                    return int(input_str)
                except BaseException:
                    print("wrong type")
            elif(type=="float"):
                try:
                    return float(input_str)
                except BaseException:
                    print("wrong type")
            else:
                return input_str

    safe_input("enter:","int")
    ```

3. Write a function named prompt_open that prompts for a file name and repeatedly attempts to read the specified file until a correctly specified file has been entered. The function takes one mode argument, 'r' or 'w', and returns the file handle that open returns.
    ```
    def prompt_open(mode):
        while True:
            f_name = input("enter filename:")
            try:
                f = open(f_name, mode)
                return f 
            except IOError:
                print("file not exist")

    f = prompt_open("r")
    f.close()
    ```
4. Write a program that prompts for three numbers. Divide the first number by the
second number and add that result to the third number. Using exceptions check for
the following errors: ValueError, and ZeroDivisionError.
    ```
    number_1 = input("Input 1st number: ")
    number_2 = input("Input 2nd number: ")
    number_3 = input("Input 3rd number: ")
    try:
        float(number_1)
        float(number_2)
        float(number_3)
        res = number_1/number_2 + number_3
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("zero division")
    ```

5. Given:
    ```
    # reverse each line of the input file in the output file
    file_str = input("Open what file:")
    find_line_str = input("Which line (integer):")

    try:
    input_file = open(file_str)  # potential user error
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
    except IOError:
    print("The file", file_str, "doesn't exist.")
    except ValueError:
    print("Line", find_line_str, "isn't a legal line number.")

    print("End of the program")
    ```

    (a) When IOError occurred the
    user had to enter a line number before the error occurred. Rewrite the code so that if a
    bad file name is entered, the error will be handled before a line number is requested.

    (b) Rewrite the code so that if IOError occurs the program keeps asking for input until the user gets it right

    (c) Rewrite the code so that if error ValueError occurs the program keeps asking for input until the user gets it right.
```py
while True:
    file_str = input("Open what file:")
    try:
        input_file = open(file_str)  # potential user error
    except IOError:
        print("The file", file_str, "doesn't exist.")
    finally:
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
print("End of the program")
```

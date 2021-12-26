from os import path         # 


# Custom error definition for custom check methods
class Error(Exception):
    pass


# Custom error definition for custom check methods
class MyError1(Error):
    pass


# Custom error definition for custom check methods
class MyError2(Error):
    pass


'''
Name:   InputCheckList

Access: public

Description:
    Method used to verify that an input is correct given a list of string of accepted values, 
    with error handling and exceptions

Parameters:
    message     string          Text of the request to be printed on the screen
    check	    list[string]    List of accepted responses
    error	    str             Text to print in case of input not relevant to the check

Returns:
    result      string
'''
def InputCheckList(message: str, check: list[str], error: str) -> str:
    while (True):
        try:
            result = input(message).upper()
            for i in result:
                if i not in check:
                    raise
            break
        except:
            if(error != ""):
                print(error + ", you can select only:")
            else:
                print("This caracter is non accptable, you can select only " + str(check))
    print()
    return result


'''
Name:   InputCheckLength

Access: public

Description:
    Method used to verify that an input is correct given a list of string of accepted values, 
    the max length and with error handling and exceptions

Parameters:
    message     string          Text of the request to be printed on the screen
    check	    list[string]    List of accepted responses
    maxLength	int             The max string length accepted

Returns:
    result      string
'''
def InputCheckLength(message: str, check: list[str], maxLength: int) -> str:
    while (True):
        try:
            result = input(message)

            for i in check:                                         # Check if the string is already in the lis befaure because it is restrictive case,
                if result == i:                                     # two can have the same length, with this order I can be more efficent
                    raise MyError1

            if len(result) > maxLength:
                raise MyError2
            break

        except MyError1:
            print("This character is already taken, choose another one!")
        except MyError2:
            print("The max number of character is " + maxLength + "!")
            print("You have insert " + len(result) + " character!")
        except:
            print("This is not an acceptable character!")
    print()
    return result


'''
Name:   InputCheckBool

Access: public

Description:
    Method used to verify that an input is correct given a list of string of accepted values 
    and with error handling and exceptions

Parameters:
    message     string          Text of the request to be printed on the screen
    check	    list[string]    List of accepted responses
    error	    str             Text to print in case of input not relevant to the check

Returns:
    result      bool
'''
def InputCheckBool(message: str, check: list[str], error: str) -> bool:
    result = True
    s = InputCheckList(message, check, error)
    if (s == "N"):
        result = False
    print()
    return result


'''
Name:   InputCheckNumber

Access: public

Description:
    Method used to verify that an input is a number

Parameters:
    message     string          Text of the request to be printed on the screen

Returns:
    result      int
'''
def InputCheckNumber(message: str) -> int:
    while (True):
        try:
            result = int(input(message))
            break
        except:
            print("That's not a number!")
    print()
    return result


'''
Name:   InputCheckNumberList

Access: public

Description:
    Method used to verify that an input is correct given a list of number of accepted values, 
    with error handling and exceptions

Parameters:
    message     string          Text of the request to be printed on the screen
    check	    list[int]       List of accepted responses
    error	    str             Text to print in case of input not relevant to the check

Returns:
    result      int
'''
def InputCheckNumberList(message: str, check: list[int], error: str) -> int:
    while (True):
        try:
            result = int(input(message))
            if result not in check:
                raise MyError1
            break
        except MyError1:
            print(error + ", you can select only: " + str(check))
        except:
            print("This is not a number!")
    print()
    return result


'''
Name:   InputCheckNumberAndString

Access: public

Description:
    Method used to verify that an input is correct given a list of number of accepted values, 
    with error handling and exceptions

Parameters:
    message     string          Text of the request to be printed on the screen
    check	    list[string]    List of accepted responses
    error	    str             Text to print in case of input not relevant to the check

Returns:
    result      int
'''
def InputCheckNumberAndString(message: str, check: list[str], error: str) -> int:
    while (True):
        result = input(message)
        try:
            result = int(result)
            if result < 0:
                raise MyError1
            break
        except MyError1:
            print("This is not a valid number of iterations, it must be greater than or equal to 0!\n")
        except:
            if result in check:
                result = -1
                break
            print(error + ", you can select only a number or: " + str(check))
    print()
    return result


'''
Name:   InputCheckPath

Access: public

Description:
    Method used to verify that an input is a valid path

Parameters:
    message     string          Text of the request to be printed on the screen

Returns:
    result      str
'''
def InputCheckPath(message: str) -> str:
    while (True):
        try:
            result = input(message)
            if not path.exists(result):
                raise
            break
        except:
            print("The folder location: "+ result + " does not exist, enter a valid path")
    print()
    return result


'''
Name:   InputCheckFile

Access: public

Description:
    Method used to verify that an input is a valid path

Parameters:
    message     string          Text of the request to be printed on the screen
    path        string          The folder's path

Returns:
    result      list[str]
'''
def InputCheckFile(message: str, path: str) -> list[str]:
    while (True):
        result = []
        try:
            result.append(input(message))
            for i in result[0]:
                if i < "a" and i > "z":
                    if i < "A" and i > ">":
                        if i < "0" and i > "9":
                            raise MyError1
            result[0] += ".txt"

            start = 1
            if path.exists(path + "/" + result):
                start = InputCheckNumberList(
                    "In the folder there is already a this file's 'name, how you want to proceed:\n" +
                    "1) Overwrite it;\n" +
                    "2) Add to the end of the file;\n"+
                    "3) Change file\n"
                    [1, 2, 3],
                    "Value not accepted")

            match start:
                case 1: result.append("w")
                case 2: result.append("a")
                case 3: raise MyError2
            break
        except MyError1:
            print("The file name must not contain special characters or punctuation!")
        except MyError2:
            print("Tell me the file name")
        except:
            print("The folder location: "+ result + " does not exist, enter a valid path!")
    print()
    return result

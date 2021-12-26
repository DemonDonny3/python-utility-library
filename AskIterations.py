from InputCheck import *     # Import the custom library for checking the input

def SetIterations():
    iterations = InputCheckNumberAndString(                         # Are asked how many times to run the code
        "How many times do I have to run the program:\n" +
        "1) Write a number N and the program will be executed N times;\n" +
        "2) type E to run the code in endless mode (Will be asked to terminate at the end of all iterations);\n",
        ["e"],
        "This is neither a number nor an accepted character"
        )

    return iterations
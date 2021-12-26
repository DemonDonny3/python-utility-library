from Library.InputCheck import *     # Import the custom library for checking the input


'''
Name:   InputCheckLength

Access: public

Description:
    Method used to taking the initial config about how to use the data from the process

Parameters:
    config      dictionary      The configuration

Returns:

'''
def AskEnd(config: dict):
    config["visible"] = InputCheckBool("Select if you want to watch the process or not, type for:\n" +
                                      "Y) Yes;\n" +
                                      "N) No;\n",
                                      ["Y", "N"],
                                      "This input is invalid")

    start = InputCheckBool("Select if you want to save the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "This input is invalid")
    if(start):
        path = InputCheckPath("Tell me the path where to save records")
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")
        path += start[0]
        config["save"] = [path, start[1]]                                                            # Set the file's path
    return
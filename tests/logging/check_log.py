N_W = 6

CL = [
    "Log file initialised (*)",
    "Python interpreter path: ",
    "Python version: 3.10.7",
    "ParUtils version: 1.0.0",
    "This will be logged in a file",
]

CL_NOT = [
    "This won't be logged in a file",
]

CL_0 = [
    "Expression 'This won't be logged in a file' couldn't be found in log file",
    "Expression 'Log file initialised (*)' was found in log file",
    "Expression 'Python interpreter path: ' was found in log file",
    "Expression 'Python version: 3.10.7' was found in log file",
    "Expression 'ParUtils version: 1.0.0' was found in log file",
    "Expression 'This will be logged in a file' was found in log file",
]

CL_1 = CL_0 + [f"check_log ended with {N_W} warnings"]
CL_2 = CL_0 + [f"check_log ko, too many warnings ({N_W} warnings)"]

CL_END = [
    "Test log input",
    "user command",
    "5 elements appended in * ms. 20 elements appended in total.",
    "out_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]",
    "Examples of duplicates (limited to 5)",
    "	key1: value1",
    "	key2: value2",
    f"[ttry] Exception caught match expected ('check_log ko, too many warnings ({N_W} warnings)')",
    "Expression matched: Log file initialised (*)",
]

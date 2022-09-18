# This directory contains input, output, log, and temporary files folders.
FILES_DIR = 'PT/'

# DEBUG = True enables function decorator in utils.deco
# it basically terminates the program if one of the threads
# (or the main thread) throws an exception and prints the exception (full trace)
# in the current log file.
# Warning: DEBUG = True will make pytest fail!
DEBUG = False

# Default format for the log function
LOG_FORMAT = '%H:%M:%S -'

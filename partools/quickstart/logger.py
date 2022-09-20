# This script shows you simple examples of use for the log and step_log functions
import time
from partools.logging import Logger
from partools.logging import log
from partools.logging import log_print
from partools.logging import step_log


log("This won't be logged in a file")
Logger('TEST')
log("This will be logged in a file")

out_list = []
for i in range(1, 21):
    time.sleep(0.05)  # simulates io / calculation
    out_list.append(i)
    step_log(i, 5, "elements appended")

log_print(f'out_list: {out_list}')

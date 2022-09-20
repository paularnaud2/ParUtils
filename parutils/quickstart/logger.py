# This script shows you simple examples of use for the log and step_log functions
import time
from parutils.logging import Logger
from parutils.logging import log
from parutils.logging import log_print
from parutils.logging import step_log
from parutils.logging import init_sl_timer


log("This won't be logged in a file\n")

Logger('TEST')
log("This will be logged in a file\n")

log_print('step_log test', dashes=100)
out_list = []
init_sl_timer()
for i in range(1, 21):
    time.sleep(0.05)  # simulates io / calculation
    out_list.append(i)
    step_log(i, 5, "elements appended")

log_print('\nout_list:', out_list)

# This script shows you simple examples of use for the log and step_log functions
import time
import parutils as u


u.log("This won't be logged in a file\n")

u.Logger('TEST')
u.log("This will be logged in a file\n")

u.log_print('step_log test', dashes=100)
out_list = []
u.init_sl_timer()
for i in range(1, 21):
    time.sleep(0.05)  # simulates io / calculation
    out_list.append(i)
    u.step_log(i, 5, "elements appended")

u.log_print('\nout_list:', out_list)

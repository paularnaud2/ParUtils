from threading import RLock
from partools import string

from .main import log

lock = RLock()
sl_time_dict = {}


def step_log(counter,
             step,
             what='lines written',
             th_name='DEFAULT',
             extra=''):
    """Logs something only when the 'counter' is a multiple of 'step'

    - For simple use, initialise with init_sl_time()
    - For multithreaded use, initialise with gen_sl_detail(q_name)
    - For more info, check out the README.md file
    """
    if counter <= 1 or th_name not in sl_time_dict:
        init_sl_time(th_name)

    if counter % step != 0:
        return False

    st = sl_time_dict[th_name]
    dstr = string.get_duration_string(st)
    bn_1 = string.big_number(step)
    bn_2 = string.big_number(counter)
    s = "{bn1} {what} in {dstr}. {bn2} {what} in total{extra}."
    msg = s.format(bn1=bn_1, bn2=bn_2, dstr=dstr, what=what, extra=extra)

    log(msg)
    init_sl_time(th_name)

    return True


def init_sl_time(th_name):
    """Initialises the timer for the step_log function (simple use)"""
    from time import time

    with lock:
        sl_time_dict[th_name] = time()

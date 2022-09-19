from threading import RLock
from partools import string

from .main import log

lock = RLock()
sl_time_dict = {}
sl_detail = {}


def step_log(counter, step, what='lines written', nb=0, th_name='DEFAULT'):
    """Logs something only when the 'counter' is a multiple of 'step'

    For simple use, initialise with init_sl_time()

    For multithreaded use, initialise with gen_sl_detail(q_name)

    For more info, check out the README.md file
    """

    if counter % step != 0:
        return False

    detail = sl_detail[th_name] if th_name in sl_detail else ''
    st = sl_time_dict[th_name]
    dstr = string.get_duration_string(st)
    bn_1 = string.big_number(step)
    bn_2 = string.big_number(counter)
    if nb == 0:
        s = "{bn1} {what} in {dstr}. {bn2} {what} in total{detail}."
        s = s.format(bn1=bn_1, bn2=bn_2, dstr=dstr, what=what, detail=detail)
    else:
        bn_3 = string.big_number(nb)
        s = what.format(bn_1=bn_1, dstr=dstr, bn_2=bn_2, bn_3=bn_3)

    log(s)
    init_sl_time(th_name)

    return True


def init_sl_time(th_name='DEFAULT'):
    """Initialises the timer for the step_log function (simple use)"""
    from time import time

    with lock:
        sl_time_dict[th_name] = time()


def gen_sl_detail(q_name='', th_nb=1, multi_th=False):
    """Initialises the timer for the step_log function (multithread use)"""

    if q_name not in ['', 'MONO'] and multi_th is True:
        detail = f" for query '{q_name}' (connection no. {th_nb})"
    elif q_name not in ['', 'MONO']:
        detail = f" for query '{q_name}'"
    elif multi_th is True:
        detail = f" (thread no. {th_nb})"
    else:
        detail = ''

    th_name = f'{q_name}_{th_nb}'
    with lock:
        sl_detail[th_name] = detail

    init_sl_time(th_name)
    return th_name

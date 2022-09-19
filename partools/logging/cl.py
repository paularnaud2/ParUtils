from partools import file
from partools import string

from .main import log
from .main import log_print
from .main import get_logger


def check_log(in_list, log_match=False, max_warn=5):
    """Checks whether the current log file contains the 'in_list' elements.
    If it doesn't, a warning is thrown.

    - log_match: if True, the matches are printed out in the log file
    """
    import warnings

    logger = get_logger()
    log('check_log...')
    txt = file.load_txt(logger.log_path, False)
    n_w = 0
    for elt in in_list:
        m = string.like(txt, elt)
        if not m:
            n_w += 1
            s = f"Expression '{elt}' couldn't be found in log file {logger.log_path}"
            log(s, c_out=False)
            warnings.warn(s)
        elif str(m) != 'True' and log_match:
            log_print(m)

    if n_w == 0:
        log('check_log ok')
    elif n_w <= max_warn:
        log(f'check_log ended with {n_w} warnings')
    else:
        s = f'check_log ko, too many warnings ({n_w} warnings)'
        log(s)
        raise Exception(s)

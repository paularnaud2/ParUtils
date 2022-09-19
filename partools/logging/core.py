from .logger import Logger


def log(*args, level=0, c_out=True, channel='default'):
    logger = get_logger(channel)
    logger.log(*args, level=level, c_out=c_out)


def log_print(*args, level=0, c_out=True, nb_tab=0, dashes=0, channel='default'):
    logger = get_logger(channel)
    logger.log_print(*args, level=level, nb_tab=nb_tab, c_out=c_out, dashes=dashes)


def get_logger(channel='default', force_init=False) -> Logger:
    from .g import loggers

    if channel not in loggers:
        logger = Logger()
        loggers[channel] = logger
    else:
        logger = loggers[channel]
    return logger


def log_array(array, nb_tab=0):
    for elt in array:
        log_print(elt, nb_tab)


def log_dict(dict, nb_tab=0):
    for key in dict:
        log_print(f'{key}: {dict[key]}', nb_tab)


def log_example(list_in, what="duplicates", n_print=5):
    if not list_in:
        return

    log_print(f"Examples of {what} (limited to {n_print}):")
    log_array(list_in[:n_print])

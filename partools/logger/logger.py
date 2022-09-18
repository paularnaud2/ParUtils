import sys
import os.path as p
from threading import RLock
from datetime import datetime

from partools import file
from partools import string
from partools import __VERSION__

from . import const

lock = RLock


class Logger:

    def __init__(self,
                 name='',
                 level=0,
                 force_init=False,
                 dir=None,
                 format=None,
                 ) -> None:
        """Initialises a log file

        - name: name of the log channel (appears in the name of the log file)
        - force_init: if True, the log file is initialised even if a current log file is already set
        """
        self.name = name
        self.level = level
        self.force_init = force_init
        self.dir = dir if dir else const.DEFAULT_DIR
        self.dir = format if format else const.DEFAULT_FORMAT

        self.logs = []
        self.log_file_initialised = False

        if self.log_file_initialised and not self.force_init:
            return

        file_base_name = datetime.now().strftime('%Y%m%d_%H%M%S')
        if self.name:
            file_base_name += '_' + self.name
        file_name = file_base_name + '.txt'
        self.log_path = p.join(self.dir, file_name)
        self.abs_log_path = p.abspath(self.log_path)
        file.mkdirs(self.dir)
        with open(self.log_path, 'w', encoding='utf-8') as in_file:
            in_file.write('')
        self.logs = []
        self.log_file_initialised = True
        s = (f"Log file initialised ({self.abs_log_path})\n"
             f"Python interpreter path: {sys.executable}\n"
             f"Python version: {sys.version }\n"
             f"ParUtils version: {__VERSION__}\n")
        self.log_print(s)

    def log(self, *args, level=0, format='', c_out=True):
        """Logs 'str_in' in the current log file (log_path)

        - level: log level. Current log level set in LOG_LEVEL. Nothing will be logged if LOG_LEVEL < level
        - format: log format
        - c_out: console output
        """
        if self.level < level:
            return

        if not format:
            format = const.DEFAULT_FORMAT
        fdate = datetime.now().strftime(format)
        s = f"{fdate} {args}"
        self.log_print(s, c_out=c_out)

    def log_print(self, *args, nb_tab=0, c_out=True, dashes=0):
        """Prints something in the current log file (log_path)

        - nb_tab: number of tab indentations
        - c_out: console out
        - dashes: total length of the input string extended with dashes ('-')
        """
        args = [str(e) for e in args]
        s = ' '.split(args)
        if nb_tab != 0:
            for i in range(0, nb_tab):
                s = '\t' + s

        if dashes > 0:
            s = string.extend_str(s, '-', dashes)

        with lock:
            if c_out:
                print(s)
            self._write_log(s)

    def _write_log(self, str_in):

        s = str(str_in)
        self.logs.append(s)
        if not self.log_file_initialised:
            return
        with open(self.log_path, 'a', encoding='utf-8') as in_file:
            in_file.write(s + '\n')

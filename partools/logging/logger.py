import sys
import os.path as p
from threading import RLock
from datetime import datetime

from partools import file
from partools import string
from partools import __VERSION__

from . import const
from .g import loggers

lock = RLock()


class Logger:

    def __init__(self,
                 name='',
                 channel='default',
                 level=None,
                 dir=None,
                 format=None,
                 file_write=False,
                 ) -> None:
        """Initialises a logger

        - file_write: if True, a file is initialised in which the logger saves the logs
        """
        self.logs = []
        self.name = name
        self.channel = channel
        self.level = level if level else const.DEFAULT_LEVEL
        self.dir = dir if dir else const.DEFAULT_DIR
        self.format = format if format else const.DEFAULT_FORMAT
        self.file_write = file_write

        if not file_write:
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
        s = (f"Log file initialised ({self.abs_log_path})\n"
             f"Python interpreter path: {sys.executable}\n"
             f"Python version: {sys.version }\n"
             f"ParUtils version: {__VERSION__}\n")
        self.log_print(s)
        loggers[channel] = self

    def log(self, *args, level=0, c_out=True):
        """Logs 'str_in' in the current log file (log_path)

        - level: log level. Current log level set in LOG_LEVEL. Nothing will be logged if LOG_LEVEL < level
        - format: log format
        - c_out: console output
        """
        if self.level < level:
            return

        args = [str(e) for e in args]
        msg = ' '.join(args)
        fdate = datetime.now().strftime(self.format)
        s = f"{fdate}{msg}"
        self.log_print(s, c_out=c_out)

    def log_print(self, *args, level=0, c_out=True, nb_tab=0, dashes=0):
        """Prints something in the current log file (log_path)

        - nb_tab: number of tab indentations
        - c_out: console out
        - dashes: total length of the input string extended with dashes ('-')
        """
        if self.level < level:
            return

        args = [str(e) for e in args]
        s = ' '.join(args)
        if nb_tab != 0:
            for i in range(0, nb_tab):
                s = '\t' + s

        if dashes > 0:
            s = string.extend_str(s, '-', dashes)

        with lock:
            if c_out:
                print(s)
            self._write_log(s)

    def log_input(self, str_in):
        """Same as input but traced in the log file"""

        with lock:
            self._write_log(str_in)
            command = input(str_in)
            self._write_log(str_in)

        return command

    def _write_log(self, str_in):

        s = str(str_in)
        self.logs.append(s)
        if not self.file_write:
            return
        with open(self.log_path, 'a', encoding='utf-8') as in_file:
            in_file.write(s + '\n')

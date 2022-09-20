import sys
import os.path as p
from threading import RLock
from datetime import datetime

from partools import file
from partools import string
from partools import __VERSION__

from . import g
from . import const

lock = RLock()


class Logger:

    def __init__(
        self,
        file_label='',
        force_new_logger=False,
        level=None,
        log_format=None,
        file_write=True,
        dir=None,
        file_format=None,
    ) -> None:

        if g.logger and g.logger.file_write and not force_new_logger:
            self = g.logger
            return

        self.logs = []
        self.level = level if level else const.DEFAULT_LEVEL
        self.log_format = log_format if log_format else const.DEFAULT_LOG_FORMAT
        self.file_write = file_write
        if not file_write:
            return

        self.file_label = file_label
        self.dir = dir if dir else const.DEFAULT_DIR
        self.file_format = file_format if file_format else const.DEFAULT_FILE_FORMAT
        file_base_name = datetime.now().strftime(self.file_format)
        if self.file_label:
            file_base_name += '_' + self.file_label
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
        g.logger = self

    def log(self, *args, level=0, c_out=True):
        if self.level < level:
            return

        args = [str(e) for e in args]
        msg = ' '.join(args)
        fdate = datetime.now().strftime(self.log_format)
        s = f"{fdate}{msg}"
        self.log_print(s, c_out=c_out)

    def log_print(self, *args, level=0, c_out=True, nb_tab=0, dashes=0):
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

import imp
from operator import imod
from parutils import csv
from parutils import file
import parutils.dup as dup
import parutils.diff as diff
from parutils.logger import log

import tests.dup.const as const
import tests.dup.check_log as cl


def test_tools():
    log.init_log('test_tools', True)
    file.mkdirs(const.OUT_DIR, True)
    log.log_print()

    log.log_print("Test toolDup - find_dup simple", dashes=100)
    dup.find_dup(const.DUP_IN, const.DUP_OUT)
    log.log_print()
    diff.file_match(const.DUP_OUT, const.DUP_OUT_REF)

    log.log_print("Test toolDup -find_dup col", dashes=100)
    dup.find_dup(const.DUP_COL_IN, col=1)
    log.log_print()
    diff.file_match(const.DUP_OUT, const.DUP_OUT_REF)

    log.log_print("Test toolDup - del_dup + shuffle", dashes=100)
    dup.shuffle_file(const.DUP_IN, const.SHUF_OUT)
    log.log_print()
    dup.del_dup(const.SHUF_OUT, const.DUP_OUT)
    log.log_print()
    diff.file_match(const.DUP_OUT, const.DEL_DUP_OUT_REF)

    log.log_print("Test toolDup - find_dup_list", dashes=100)
    list_in = csv.load_csv(const.DUP_IN)
    dup_list = dup.find_dup_list(list_in)
    csv.save_csv(dup_list, const.DUP_OUT)
    diff.file_match(const.DUP_OUT, const.DUP_OUT_REF)

    log.check_log(cl.CL)


if __name__ == '__main__':
    test_tools()

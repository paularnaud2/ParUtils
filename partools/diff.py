import os.path as p

from partools import file
from partools.dup import del_dup_list
from partools.logger.log import log
from partools.logger.log import log_print

OUT_DIR = 'out'


def file_match(in1, in2, del_dup=False, err=True, out_path=''):
    """Compares two files and outputs the diff if the files don't match.
    Note that the files are sorted before comparison.
    (more generic than run_dq but doesn't work for big files)

    - del_dup: if true, duplicates are deleted before comparison
    - err: if True, an exception is raised when the files don't match
    - out_path: specifies an output path for file comparison different from default
    """

    log("[dq] file_match: start")

    if not out_path:
        out_path = p.join(OUT_DIR, 'file_match_out.csv')

    s = f"Comparing files '{in1}' and '{in2}'..."
    log(s)
    l1, l2 = file.load_txt(in1), file.load_txt(in2)
    l1.sort(), l2.sort()
    if del_dup:
        l1, l2 = del_dup_list(l1), del_dup_list(l2)

    res = l1 == l2
    s = "Files match" if res else "Files don't match"
    log(s)

    if not res:
        diff_list(l1, l2, out_path)
        if err:
            file.startfile(out_path)
            assert res is True

    log("[dq] file_match: end")
    log_print()


def diff_list(list1, list2, out_path):

    if not out_path:
        out_path = p.join(OUT_DIR, 'file_match_out.csv')

    out1 = [e for e in list1 if e not in list2]
    out2 = [e for e in list2 if e not in list1]
    out = del_dup_list(out1 + out2)
    file.save_list(out, out_path)
    log(f"Comparison result available here: {out_path}")

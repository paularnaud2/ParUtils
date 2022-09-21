import parutils as u

FILES_DIR = 'tests/dq/files/'
OUT_DIR = 'out/tests/'
DUP_IN = FILES_DIR + 'dup_in.csv'
DUP_OUT = OUT_DIR + 'out_dup.csv'
DUP_OUT_REF = FILES_DIR + 'dup_out_ref.csv'


def test_dq():
    u.Logger('TEST_DQ', True)
    u.file.mkdirs(OUT_DIR, True)
    u.log_print()

    u.log_print("Test toolDup - find_dup_list", dashes=100)
    list_in = u.load_csv(DUP_IN)
    dup_list = u.find_dup_list(list_in)
    u.log_example(dup_list)
    u.save_csv(dup_list, DUP_OUT)
    u.file_match(DUP_OUT, DUP_OUT_REF)


if __name__ == '__main__':
    test_dq()

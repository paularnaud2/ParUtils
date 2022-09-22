import parutils as u


def test_file():
    u.mkdirs('')

    assert u.list_files('not exist') == []
    assert len(u.list_files('parutils')) > 1
    out = u.list_files('parutils', only_list=['dq', 'c'], ignore_list=['msc'])
    assert out == ['parutils/csv.py', 'parutils/dq.py']

    path = 'out/tests/out.txt'
    u.save_list(out, path)
    assert u.count_lines(path) == 2


if __name__ == '__main__':
    test_file()

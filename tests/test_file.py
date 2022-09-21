import parutils as u


def test_file():
    u.mkdirs('')

    assert u.list_files('not exist') == []
    out = u.list_files('parutils', only_list=['c'], ignore_list=['msc'])
    assert out == ['parutils/csv.py']

    path = 'out/tests/out.txt'
    u.save_list(out, path)
    assert u.count_lines(path) == 1


if __name__ == '__main__':
    test_file()

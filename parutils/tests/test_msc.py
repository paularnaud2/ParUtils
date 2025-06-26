import parutils as u


def test_msc():
    lst = ['key1=value1', 'key2=value2']
    out = u.list_to_dict(lst)

    d = {'key1': 'value1', 'key2': 'value2'}
    assert out == d

    out = u.replace_from_dict('Hello @@VAR@@', {'VAR': 'world'})
    assert out == 'Hello world'

    u.ttry(nok_func, 'test_error')
    err = "[ttry] Exception caught ('test_error') don't match expected ('test_error_1')"
    u.ttry(u.ttry, err, nok_func, 'test_error_1')
    u.ttry(u.ttry, "[ttry] No exception was caught", ok_func, 'test_error')

    with u.Wtry('test_error'):
        nok_func()
    with u.Wtry("[Wtry] No exception was caught"):
        with u.Wtry('test_error'):
            ok_func()
    err = "[Wtry] Exception caught ('test_error') don't match expected ('test_error_1')"
    with u.Wtry(err):
        with u.Wtry('test_error_1'):
            nok_func()


def nok_func():
    raise Exception('test_error')


def ok_func():
    pass


if __name__ == '__main__':  # pragma: no cover
    test_msc()

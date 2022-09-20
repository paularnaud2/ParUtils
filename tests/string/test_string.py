import parutils as u
from tests.string.check_log import CL


def get_duration():
    u.log_print("Test get_duration_string", dashes=100)

    dstr = u.get_duration_string(0, end_time=0.35)
    u.log(dstr)
    assert dstr == "350 ms"

    dstr = u.get_duration_string(0, end_time=5.369)
    u.log(dstr)
    assert dstr == "5.3 s"

    dstr = u.get_duration_string(0, end_time=150)
    u.log(dstr)
    assert dstr == "2 minutes and 30 seconds"

    u.log_print()


def like():
    u.log_print("Test of like functions", dashes=100)

    s = '2 test ok?'
    assert u.like(s, 'test')
    u.log("like simple ok")

    m = u.like(s, '2 * ok?')
    assert m.group(1) == 'test'
    u.log("like m ok")

    lst = ['1', 'test']
    assert u.like_list(s, lst)
    u.log("like_list ok")

    dct = {'1': 'a', '2': 'test'}
    assert u.like_dict(s, dct) == '2'
    u.log("like_dict ok")

    u.log_print()


def test_string():
    u.Logger('TEST_STRING', True)

    get_duration()
    like()
    u.check_log(CL)

    u.log_print()


if __name__ == '__main__':
    test_string()

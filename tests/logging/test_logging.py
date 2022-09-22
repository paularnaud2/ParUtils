# This script shows you simple examples of use for the log and step_log functions
import time
import pytest
import parutils as u
from tests.logging import check_log as cl


def test_logging(monkeypatch):

    u.get_logger().close()
    u.log("This won't be logged in a file\n")
    e_ref = "No log file has been initialised"
    u.ttry(u.check_log, e_ref, cl.CL)
    u.log_print()

    u.Logger('TEST_LOGGING_1')
    u.Logger()
    u.log("This will be logged", "in a file\n")
    u.check_log(cl.CL, cl.CL_NOT)

    with pytest.warns(UserWarning):
        u.check_log(cl.CL_NOT, cl.CL, max_warn=10)
        u.check_log(cl.CL_1)
    u.get_logger().close()

    u.Logger('TEST_LOGGING_2')
    u.log("This will be logged", "in a file\n")
    u.log("This won't be logged in a file\n", level=1)
    u.log_print("This won't be logged in a file\n", level=1)
    with pytest.warns(UserWarning):
        e_ref = f"check_log ko, too many warnings ({cl.N_W} warnings)"
        u.ttry(u.check_log, e_ref, cl.CL_NOT, cl.CL)
        u.check_log(cl.CL_2)

    monkeypatch.setattr('builtins.input', mock_input)
    assert u.log_input("Test log input") == "user command"

    u.log_print('step_log test', dashes=100)
    out_list = []
    u.init_sl_timer()
    for i in range(1, 21):
        # time.sleep(0.05)  # simulates io / calculation
        out_list.append(i)
        u.step_log(i, 5, "elements appended")

    u.log_print('\nout_list:', out_list)
    u.log_example(out_list)
    u.log_example([])
    d = {'key1': 'value1', 'key2': 'value2'}
    u.log_dict(d, nb_tab=1)

    u.check_log(cl.CL, log_matches=True)
    u.check_log(cl.CL_END)

    u.get_logger().close()


def mock_input(txt):
    out = "user command"
    print(txt + out)
    return out


if __name__ == '__main__':
    import conftest
    from _pytest.monkeypatch import MonkeyPatch
    u.logging.const.DEFAULT_DIR = conftest.TESTS_LOG_DIR

    test_logging(MonkeyPatch())

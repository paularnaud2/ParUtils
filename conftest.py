import pytest
import parutils as u
import parutils.logging.const as const


@pytest.fixture(scope="session", autouse=True)
def prepare(request):
    tests_log_dir = 'log/tests'
    const.DEFAULT_DIR = tests_log_dir
    u.mkdirs(tests_log_dir, True)

    # request.addfinalizer(finalizer_function)

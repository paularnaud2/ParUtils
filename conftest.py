import pytest
import parutils as u
import parutils.logging.const as const

TESTS_LOG_DIR = 'log/tests'
TESTS_OUT_DIR = 'out/tests'


@pytest.fixture(scope="session", autouse=True)
def before_all(request):
    const.DEFAULT_DIR = TESTS_LOG_DIR
    u.mkdirs(TESTS_LOG_DIR, True)
    u.mkdirs(TESTS_OUT_DIR, True)

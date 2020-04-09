# 
import time

import pytest

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

@pytest.fixture(autouse=True)
def timer_session_scope():
    start = time.time()
    print('\nstart:{}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))
    yield
    finished = time.time()
    print('\nfinished:{}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    
    
def test_1():
    time.sleep(1)
    
    
# pytest -s  pytest_fixture_autouse.py  # -s会将print的输出打印到控制台
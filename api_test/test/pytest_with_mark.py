# test_with_mark.py
import pytest

@pytest.mark.finished
def test_func1():
    assert 1==1

@pytest.mark.unfinished
def test_func2():
    assert 1!=1
@pytest.mark.nothing
def test_func3():
    assert 'a' == 'b'
    
    
# 在命令行运行pytest -m  finished  test_with_mark.py  h

# 结果会显示1 passed, 2 deselected,

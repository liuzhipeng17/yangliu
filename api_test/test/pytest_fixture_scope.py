# pytest scope
import pytest


# scope参数，可指定fixture的作用域
# function, 每个测试函数都会执行一遍（以test开头的函数)
# class,    每个测试类执行一次
# module,   每个模块执行一次
# session,  一次测试只执行一次，

@pytest.fixture(scope='function')
def func_scope():
    pass

@pytest.fixture(scope='class')
def class_scope():
    pass
    
@pytest.fixture(scope='module')
def mod_scope():
    pass
    
@pytest.fixture(scope='session')
def sess_scope():
    pass

def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass

# pytest --setup-show  pytest_fixture.py  # --setup-show可以看到执行的顺序
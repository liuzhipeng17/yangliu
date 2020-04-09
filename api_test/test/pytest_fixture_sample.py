#pytest fixture, 作为参数执行

import pytest
'''
@pytest.fixture()
def postcode():
    return '010'

def test_postcode(postcode):
    assert postcode == '010'
'''
# fixture是一些函数， pyttest会在执行函数之前或之后加载它们。
# 固件可以直接z定义在各测试脚本中。
# 或者，使用conftest.pyl集中管理fixture，conftest.py的作用域是所在的目录和子目录
# 不需要显示调用conftest.py
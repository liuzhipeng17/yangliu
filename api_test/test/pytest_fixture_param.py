# fixture 本身是函数，函数就可以参数化
''' function的参数化

@pytest.mark.parametrize('passwd', ['123456',
                                    'abcdefdfs'
                                    'asdsfsdf'])
def test_password_length(passwd):
    assert len(passwd) == 6

'''




# 假设有一批api需要测试不同数据库的支持情况。
# 使用fixture抽离出数据库的通用操作，每个api都能服用数据库固件
# fixture 函数的参数化需要内置的固件request，并通过request.param获取参数

import pytest 


# 下面是fixture 函数的参数化， 和function的参数化不一样


@pytest.fixture(params=[('redis', '6379'),
                        ('elasticsearch', '9200')])
def param(request):
    return request.param  
    
@pytest.fixture(autouser=True)    
def db(param):
    print('\nSucceed to connect %s:%s' % param)
    yield
    print('\nSucceed to close %s:%s' % param)
    
    
    
def test_api():
    assert 1==1
    
    
    
# 补充一个函数的参数化
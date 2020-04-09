import pytest

@pytest.fixture(name='age')
def calculate_average_age():
    return 28
    
    
def test_age(age):    #age是fixture， fixture默认是函数名， name参数可以重命名fixture
    assert age == 28
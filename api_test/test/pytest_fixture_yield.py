import pytest


# fixture实现数据预处理和后处理
# pytest使用yield将fixture分为两部分，yield之前的代码属于预处理， yield后面的代码属于后处理 

@pytest.fixture()
def db():
    print('Connection successful')
    yield
    print('Connection closed')

def search_user(user_id):
    d = {'001': 'xiaoming'}
    return d[user_id]

def test_search(db):
    assert search_user('001') == 'xiaoming'


# pytest -s  pytest_fixture.py



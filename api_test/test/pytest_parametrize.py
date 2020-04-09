import pytest

@pytest.mark.parametrize('password', ['123456', 'abdfdafdf','afafefe'])
def test_password_length(password):
    assert len(password) == 6


@pytest.mark.parametrize('user, password',[pytest.param('jack', 'abcdefgh', id='User<Jack>'),
                                             pytest.param('tom','a123456a', id='User<Tom>')])
def test_password_md5_id(user, password):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
        }
    import hashlib

    assert hashlib.md5(password.encode()).hexdigest() == db[user]



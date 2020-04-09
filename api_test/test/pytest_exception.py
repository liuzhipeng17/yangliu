import pytest

def test_raises():
    with pytest.raises(Exception) as e:
        1/0
    msg = e.value.args[0]
    print(msg)
    assert msg == "division by zero"


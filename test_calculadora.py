import pytest

def multiplica(num1, num2):
    return 0


@pytest.mark.parametrize('num1, num2, valoresperado', [(0, 0, 0)])
def test_multiplica(num1, num2, valoresperado):
    assert multiplica(num1, num2) == valoresperado


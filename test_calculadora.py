import pytest

def multiplica(num1, num2):
    pass


@pytest.mark.parametrize('num1, num2, valoresperado', [0, 0, 0])
def test_multiplica(num1, num2, valoresperado):
    assert multiplica(num1, num2) == valoresperado


import pytest

def multiplica(valor1, valor2):
    return 0


@pytest.mark.parametrize('valor1, valor2, valor_esperado', [(0, 0, 0)])
def test_multiplica(valor1, valor2, valor_esperado):
    assert multiplica(valor1, valor1) == valor_esperado


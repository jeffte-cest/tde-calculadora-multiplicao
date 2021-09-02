import pytest

def multiplica(valor1, valor2):
    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao

@pytest.mark.parametrize('valor1, valor2, valor_esperado', [(0, 0, 0), [1, 1, 1]])
def test_multiplica_com_parametros_validos(valor1, valor2, valor_esperado):
    assert valor1 * valor2 == valor_esperado
    assert multiplica(valor1, valor2) == valor_esperado

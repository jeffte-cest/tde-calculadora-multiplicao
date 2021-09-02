import pytest

def multiplica(valor1 = 0, valor2 = 0):
    valor1 = valor1 or 0
    valor2 = valor2 or 0
    
    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao

@pytest.mark.parametrize('valor1, valor2, valor_esperado', [(0, 0, 0), [1, 1, 1]])
def test_multiplica_com_parametros_validos(valor1, valor2, valor_esperado):
    assert valor1 * valor2 == valor_esperado
    assert multiplica(valor1, valor2) == valor_esperado

@pytest.mark.parametrize('valor_invalido1, valor_invalido2, valor_esperado', [(None, None, 0), ('um', 'dois', 'dois')])
def test_multiplica_com_parametros_invalidos(valor_invalido1, valor_invalido2, valor_esperado):
    assert multiplica(valor_invalido1, valor_invalido2) == valor_esperado

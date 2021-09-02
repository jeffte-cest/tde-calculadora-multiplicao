import pytest

def multiplica(valor1, valor2):
    isParametroUmNumerico = type(valor1) is int or type(valor1) is float

    if(not isParametroUmNumerico):
        raise Exception("parametro 1 eh invalido")

    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao

@pytest.mark.parametrize('valor1, valor2, valor_esperado', [(0, 0, 0), [1, 1, 1]])
def test_multiplica_com_parametros_validos(valor1, valor2, valor_esperado):
    assert valor1 * valor2 == valor_esperado
    assert multiplica(valor1, valor2) == valor_esperado

def test_multiplica_com_parametro1_invalido():
    with pytest.raises(Exception) as excinfo:  
        parametro_invalido = "qualquer valor"
        parametro_valido = 2

        multiplica(parametro_invalido, parametro_valido)
    
    assert excinfo.value.message == "parametro 1 eh invalido"

    

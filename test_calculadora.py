import pytest

def multiplica(valor1, valor2):
    isParametroUmNumerico = type(valor1) is int or type(valor1) is float
    isParametroDoisNumerico = type(valor2) is int or type(valor2) is float

    if(not isParametroUmNumerico):
        raise Exception("parametro 1 eh invalido")
    
    if(not isParametroDoisNumerico):
        raise Exception("parametro 2 eh invalido")

    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao

@pytest.mark.parametrize('valor1, valor2, valor_esperado', [(0, 0, 0), [1, 1, 1], (2, 2, 4), (5, 0.5, 2.5)])
def test_multiplica_com_parametros_validos(valor1, valor2, valor_esperado):
    assert valor1 * valor2 == valor_esperado
    assert multiplica(valor1, valor2) == valor_esperado

def test_multiplica_com_parametro1_invalido():
    with pytest.raises(Exception):  
        parametro_invalido = "qualquer valor"
        parametro_valido = 2

        multiplica(parametro_invalido, parametro_valido)

def test_multiplica_com_parametro2_invalido():
    with pytest.raises(Exception):  
        parametro_valido = 2
        parametro_invalido = "qualquer valor"

        multiplica(parametro_valido, parametro_invalido)

    
def test_multiplica_sem_parametro1():
    with pytest.raises(Exception):
        parametro_valido = 2
        
        multiplica(None, parametro_valido)

def test_multiplica_sem_parametro2():
    with pytest.raises(Exception):
        parametro_valido = 2
        
        multiplica(parametro_valido, None)

    

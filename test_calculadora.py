import pytest
from calculadora import multiplica

def media_aritimetica(valores):
  soma_dos_valores = 0
  total_de_valores_informados = len(valores)

  for valor in valores:
    soma_dos_valores += valor
  
  media_aritimetica = soma_dos_valores/total_de_valores_informados

  return media_aritimetica

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

@pytest.mark.parametrize('valores, media', [([7,7], 7), ([1,2,3,4,5,6,7,8,9], 5)])
def test_media_aritimetica_com_valores_validos(valores, media):
        assert media_aritimetica(valores) == media

def test_media_aritimetica_com_parametro_invalido():
  with pytest.raises(Exception):
    parametro_invalido = ['valor1', 'valor2']
    media_aritimetica(parametro_invalido) 

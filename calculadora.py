def multiplica(valor1, valor2):
    isParametroUmNumerico = type(valor1) is int or type(valor1) is float
    isParametroDoisNumerico = type(valor2) is int or type(valor2) is float

    if(not isParametroUmNumerico):
        raise Exception("parametro 1 eh invalido")
    
    if(not isParametroDoisNumerico):
        raise Exception("parametro 2 eh invalido")

    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao


def media_aritimetica(valores):
  soma_dos_valores = 0
  total_de_valores_informados = len(valores)

  for valor in valores:
    soma_dos_valores += valor
  
  media_aritimetica = soma_dos_valores/total_de_valores_informados

  return media_aritimetica


def multiplica(valor1, valor2):
    isParametroUmNumerico = type(valor1) is int or type(valor1) is float
    isParametroDoisNumerico = type(valor2) is int or type(valor2) is float

    if(not isParametroUmNumerico):
        raise Exception("parametro 1 eh invalido")
    
    if(not isParametroDoisNumerico):
        raise Exception("parametro 2 eh invalido")

    resultado_multiplicacao = valor1 * valor2
    
    return resultado_multiplicacao

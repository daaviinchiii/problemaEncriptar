def encriptar_texto(texto: str, chave: int, coluna_inicial: int) -> str:

    texto = texto.rstrip()
    tamanho_texto = len(texto)
    linhas = (tamanho_texto + chave - 1) // chave
    
    tamanho_padrao = linhas * chave
    texto = texto.ljust(tamanho_padrao)
    
    matriz = []
    for i in range(linhas):
        inicio = i * chave
        fim = inicio + chave
        matriz.append(list(texto[inicio:fim]))
    
    resultado = []
    coluna_atual = coluna_inicial - 1
    
    for _ in range(chave):
        for linha in matriz:
            resultado.append(linha[coluna_atual])
        coluna_atual = (coluna_atual + 1) % chave
    
    return ''.join(resultado)

def desencriptar_texto(texto_encriptado: str, chave: int, coluna_inicial: int) -> str:

    tamanho_texto = len(texto_encriptado)
    linhas = tamanho_texto // chave
    
    matriz = [['' for _ in range(chave)] for _ in range(linhas)]
    
    coluna_atual = coluna_inicial - 1
    indice_texto = 0
    
    for _ in range(chave):
        for linha in range(linhas):
            matriz[linha][coluna_atual] = texto_encriptado[indice_texto]
            indice_texto += 1
        coluna_atual = (coluna_atual + 1) % chave
    
    resultado = []
    for linha in matriz:
        resultado.extend(linha)
    
    return ''.join(resultado).rstrip()

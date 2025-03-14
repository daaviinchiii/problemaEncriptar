# Programa de Encriptação/Desencriptação de Texto

Este programa implementa um cifra de transposição para encriptação e desencriptação de texto. Ele lê o texto de um arquivo, encripta usando a chave e coluna inicial especificadas, e então verifica a encriptação desencriptando o texto.

## Funcionalidades

- Encriptação de texto usando método de transposição
- Desencriptação de texto
- Suporte para entrada/saída de arquivos
- Validação de entrada
- Verificação do processo de encriptação/desencriptação

## Requisitos

- Python 3.6 ou superior

## Como Usar

1. Crie um arquivo de texto com o conteúdo que deseja encriptar
2. Execute o programa:
   ```bash
   python main.py
   ```
3. Quando solicitado:
   - Digite o nome do arquivo de entrada
   - Digite a chave de encriptação (número de colunas)
   - Digite a coluna inicial (1 até a chave)

## Saída

O programa irá:
1. Ler o texto do arquivo de entrada
2. Encriptar o texto
3. Desencriptar o texto para verificação
4. Salvar o texto encriptado em `encriptado.txt`
5. Salvar o texto desencriptado em `desencriptado.txt`
6. Exibir todas as três versões (original, encriptada e desencriptada) no console

## Exemplo

Arquivo de entrada (`entrada.txt`):
```
Encriptação por transposição
```

Executando o programa com:
- Chave: 5
- Coluna inicial: 3

Produzirá:
- Texto encriptado em `encriptado.txt`
- Texto desencriptado em `desencriptado.txt`
- Saída no console mostrando todas as três versões

## Observações

- O programa utiliza codificação UTF-8 para suporte adequado de caracteres
- Todos os caracteres, incluindo quebras de linha, são considerados na encriptação
- O programa verifica se o texto desencriptado corresponde ao original

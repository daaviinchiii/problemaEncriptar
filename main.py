from encrypted import encriptar_texto, desencriptar_texto

def ler_arquivo(nome_arquivo: str) -> str:
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        exit(1)
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        exit(1)

def escrever_arquivo(nome_arquivo: str, conteudo: str) -> None:
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except Exception as e:
        print(f"Erro ao escrever arquivo: {e}")
        exit(1)

def obter_entrada_usuario() -> tuple[int, int]:
    while True:
        try:
            chave = int(input("Digite a chave de encriptação (número de colunas): "))
            if chave <= 0:
                print("A chave deve ser positiva.")
                continue
                
            coluna_inicial = int(input(f"Digite a coluna inicial (1 até {chave}): "))
            if not 1 <= coluna_inicial <= chave:
                print(f"A coluna inicial deve estar entre 1 e {chave}.")
                continue
                
            return chave, coluna_inicial
        except ValueError:
            print("Por favor, digite números válidos.")

def mostrar_menu() -> int:
    while True:
        print("\n=== Menu de Encriptação/Desencriptação ===")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção (1-3): "))
            if 1 <= opcao <= 3:
                return opcao
            print("Por favor, escolha uma opção válida (1-3).")
        except ValueError:
            print("Por favor, digite um número válido.")

def encriptar():
    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    texto = ler_arquivo(arquivo_entrada)
    chave, coluna_inicial = obter_entrada_usuario()
    
    texto_encriptado = encriptar_texto(texto, chave, coluna_inicial)
    escrever_arquivo("encriptado.txt", texto_encriptado)
    
    print("\nTexto original:")
    print(texto)
    print("\nTexto encriptado:")
    print(texto_encriptado)

def desencriptar():
    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    texto_encriptado = ler_arquivo(arquivo_entrada)
    chave, coluna_inicial = obter_entrada_usuario()
    
    texto_desencriptado = desencriptar_texto(texto_encriptado, chave, coluna_inicial)
    escrever_arquivo("desencriptado.txt", texto_desencriptado)
    
    print("\nTexto encriptado:")
    print(texto_encriptado)
    print("\nTexto desencriptado:")
    print(texto_desencriptado)

def main():
    while True:
        opcao = mostrar_menu()
        
        if opcao == 1:
            encriptar()
        elif opcao == 2:
            desencriptar()
        else:
            print("\nPrograma encerrado.")
            break

if __name__ == "__main__":
    main() 
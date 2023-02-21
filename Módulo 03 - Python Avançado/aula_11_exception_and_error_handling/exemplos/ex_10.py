nome_arquivo = 'nome_arquivo.txt'

try:
    arquivo = open(nome_arquivo, 'r')

except FileNotFoundError:
    arquivo = open(nome_arquivo, 'a')

else:
    print(nome_arquivo)
    print(f"O Arquivo {nome_arquivo} existe")

finally:
    # Realiza algum processamento no arquivo
    print(arquivo)

    # Fecha o arquivo
    arquivo.close()
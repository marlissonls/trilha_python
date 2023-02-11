nome_arquivo = 'nome_arquivo.txt'

try:
    arquivo = open(nome_arquivo, 'r')

except FileNotFoundError:
    arquivo = open(nome_arquivo, 'a')

else:
    print(f"Arquivo {nome_arquivo} já existe")

finally:
    # Realiza algum processamento no arquivo
    processa_arquivo(arquivo)

    # Fecha o arquivo
    arquivo.close()
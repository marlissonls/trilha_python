import os, sys

# pegando o nome deste arquivo
este_arquivo = os.path.realpath(__file__)
print(este_arquivo)

# pegando o diretório atual
diretorio_atual = os.path.dirname(este_arquivo)
print(diretorio_atual)

# pegando o diretório pai
diretorio_pai = os.path.dirname(diretorio_atual)
print(diretorio_pai)

sys.path.append(diretorio_pai)

#from diretorio_pai.some_package.some_module import some_function
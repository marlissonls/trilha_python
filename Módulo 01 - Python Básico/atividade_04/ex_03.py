"""
Questão 3: Implemente um programa denominado intercalador, que recebe duas strings e deve intercalá-las, 
alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira
letra da segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. 
As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada. 

Observação: Seu programa não pode usar funções pré-definidas além de print(), input(), input().split(" ") e len(). 

Dica: Utilize a função input().split(" ") para ler múltiplos elementos de uma string separadas por espaço e 
salvar em um vetor. No caso específico desse exercício, a ideia é obter um vetor de 2 strings da seguinte forma: 

palavras = input().split(" ") # lendo um vetor de múltiplas strings (palavras) separadas por espaço 

S1 = palavras[0] # obtendo a primeira string 

S2 = palavras[1] # obtendo a segunda string 

Entrada:
Uma linha contendo duas cadeias de caracteres separadas por um espaço em branco. 

Saída:
Uma cadeia de caracteres resultante da intercalação das duas cadeias fornecidas como entrada. 
"""

string = input('\nInforme duas cadeias de caracteres separadas por um espaço: ').split(' ')
S1 = string[0]
S2 = string[1]

stringRes = ''
if len(S1) < len(S2):
  for i in range(0, len(S1)):
    stringRes += S1[i]
    stringRes += S2[i]
  for j in range(i+1, len(S2)):
    stringRes += S2[j]
elif len(S2) < len(S1):
  for i in range(0, len(S2)):
    stringRes += S1[i]
    stringRes += S2[i]
  for j in range(i+1, len(S1)):
    stringRes += S1[j]
else: 
  for i in range(0, len(S1)):
    stringRes += S1[i]
    stringRes += S2[i]

print(stringRes)
"""
Questão 3: Escreva um programa que leia dois vetores com N inteiros cada. 
Em seguida, verifique quais elementos do segundo vetor são iguais a algum elemento do primeiro vetor. 
Se não houver elementos comuns, o programa deve informar isso. 

Dica: Para ler um vetor de inteiros separados por espaço de uma linha fornecida, use o comando: 

V = [int(i) for i in input().split(" ") if i] 

Entrada: Cada caso de teste é composto por duas linhas, cada uma contendo uma cadeia de N inteiros. Os valores devem ser separados por um espaço em branco. Não é necessário que as duas cadeias tenham o mesmo número de elementos. (dica: função len(V) resulta na quantidade de elementos de um vetor). 

Saída: Na saída devem ser impressos todos os elementos comuns entre os dois vetores, sendo cada elemento em uma linha diferente. Entretanto, se houver algum elemento que apareça mais de uma vez no segundo vetor, o mesmo deve ser impresso apenas uma vez. Se um elemento aparecer mais de uma vez no primeiro vetor, o mesmo pode ser impresso mais de uma vez. Caso não haja nenhum elemento em comum, a seguinte mensagem deverá ser exibida: NENHUM ELEMENTO EM COMUM. 
"""

print("\nInforme o 1º vetor de inteiros separados por um espaço: ")
V1 = [int(i) for i in input().split(' ') if i]

print("\nInforme o 2º vetor de inteiros separados por um espaço: ")
V2 = [int(i) for i in input().split(' ') if i]

print('\n')
found = False
for i in range(len(V1)):
  for j in range(len(V2)):
    if V1[i] == V2[j]:
      found = True
      print(V1[i])
      break

if found == False:
  print('NENHUM ELEMENTO EM COMUM')